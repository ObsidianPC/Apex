import getpass
import os
import re

import data as p4Data

import perforce.P4 as perforce



class TimeoutException(Exception):
    def __init__(self, message=''):
        super(TimeoutException, self).__init__(message)


def errorHandler(wrappedMethod):
    def wrapper(*args, **kwargs):
        print args[0]
        try:
            return wrappedMethod(*args, **kwargs)
        except Exception as error:
            error = str(error)
            raise Exception(error)

    return wrapper


def __getInstance():
    """
	:return: perforce.p4_27.P4.P4
	"""
    instance = perforce.P4()
    if not instance.connected():
        try:
            instance.connect()
        except Exception as error:
            if 'check $P4PORT' in str(error):
                raise Exception('Not connected to network')

    return instance


def restore(filepath, description, changelist='default', changelistId=0):
    """
	:param filepath: :class: str
	:param description: :class: str
	:param changelist: :class: str
	:param changelistId: :class: int
	:return: :class: perforce.data.Changelist
	"""
    if not isInP4(filepath) or not isDeleted(filepath):
        return
    filepath = filepath.replace('\\', '/')

    instance = __getInstance()
    depotFilepath = getDepotFilepath(filepath)

    if depotFilepath is None:
        raise Exception('No depot file path could be found in the fstat for %s' % filepath)

    changelist = None
    if changelistId == 0 and not description == 'default':
        if changelistExists(description):
            changelist = getChangelist(description)
        else:
            changelist = createChangelist(description)
    elif not description == 'default':
        if changelistWithIdExists(changelistId):
            changelist = getChangelistById(changelistId)
        else:
            changelist = createChangelist(description)

    historyDatas = instance.run('filelog', depotFilepath)
    if len(historyDatas) == 0:
        raise Exception('Not able to find revision to revert to: %s in depot at %s' % (filepath, depotFilepath))
    if len(historyDatas[0]['rev']) < 2:
        raise Exception('Not able to find revision to revert to: %s in depot at %s' % (filepath, depotFilepath))

    history = p4Data.RevisionHistory(historyDatas[0])
    revisionToRevertTo = None
    for item in history.items:
        if item.action == 'delete' or item.action == 'move/delete':
            revisionToRevertTo = item.previousRevision

    if revisionToRevertTo is None:
        raise Exception('Not able to find revision to revert to: %s in depot at %s' % (filepath, depotFilepath))

    haveRevision = -1
    fstatInfo = None
    try:
        fstatInfo = instance.run('fstat', '-T haveRev', depotFilepath)
    except Exception as error:
        if "Field haveRev doesn't exist" not in str(error):
            raise Exception('Not able to analazy have revision of file: %s. Error: %s' % (filepath, str(error)))

    if fstatInfo is not None:
        for fstatInfoData in fstatInfo:
            if 'haveRev' in fstatInfoData.keys():
                haveRevision = None if fstatInfoData['haveRev'] == 'none' else int(fstatInfoData['haveRev'])
                break

    if haveRevision is None:
        raise Exception('Current have revision is None: %s revision: %s.' % (filepath, revisionToRevertTo.revision))

    if haveRevision != revisionToRevertTo.revision:
        try:
            instance.run('sync', ('%s#%s' % (depotFilepath, revisionToRevertTo.revision)))
        except Exception as error:
            raise Exception('Not able to sync revision to revert to: %s revision: %s. Error: %s' % (
                filepath, revisionToRevertTo, str(error)))

    try:
        if changelist is None:
            instance.run('add', filepath)
        else:
            instance.run('add', '-c%s' % changelist.change, filepath)
    except Exception as error:
        raise Exception('Not able to add revision to revert to: %s revision: %s. Error: %s' % (
            filepath, revisionToRevertTo, str(error)))

    return p4Data.Changelist.getDefaultChangelist(client=instance.client,
                                                  user=instance.user) if changelist is None else changelist


def getDepotFilepath(filepath):
    """
	:param filepath: :class: str
	:return: :class: str
	"""
    instance = __getInstance()
    info = instance.run('fstat', filepath)
    if len(info) == 0:
        raise Exception('No file info could be found for %s' % filepath)

    for key, value in info[0].iteritems():
        if key == 'depotFile':
            return value.replace('\\', '/')

    return None


def getClientFilepath(filepath):
    """
	:param filepath: :class: str
	:return: :class: str
	"""
    instance = __getInstance()
    info = instance.run('fstat', filepath)
    if len(info) == 0:
        raise Exception('No file info could be found for %s' % filepath)

    for key, value in info[0].iteritems():
        if key == 'clientFile':
            return value.replace('\\', '/')

    return None


def getClientRootDirectory():
    """
	:return: :class: str
	"""
    instance = __getInstance()
    info = instance.run('info')[0]
    for key, value in info.iteritems():
        if key == 'clientRoot':
            return value


def getStreamRootDirectory():
    """
	:return: :class: str
	"""
    instance = __getInstance()
    info = instance.run('info')[0]
    for key, value in info.iteritems():
        if key == 'clientStream':
            return value


def add(filepath, description='default', changelistId=0):
    """
	:param filepath: :class: str
	:param description: :class: str
	:param changelistId: :class: int
	:return: :class: perforce.data.Changelist
	"""
    if not os.path.exists(filepath):
        raise Exception('Critical Error: File - %s - does not exist on the local file system.' % filepath)

    if isInP4(filepath) and isDeleted(filepath):
        restore(filepath)

    changelist = None
    if changelistId == 0 and not description == 'default':
        if changelistExists(description):
            changelist = getChangelist(description)
        else:
            changelist = createChangelist(description)
    elif not description == 'default':
        if changelistWithIdExists(changelist):
            changelist = getChangelistById(changelistId)
        else:
            changelist = createChangelist(description)

    instance = __getInstance()

    if changelist == None:
        instance.run('add', filepath)
    else:
        instance.run('add', '-c%s' % changelist.change, filepath)

    return p4Data.Changelist.getDefaultChangelist(client=instance.client,
                                                  user=instance.user) if changelist is None else changelist


def checkOut(filepath, description='default', force=False, doSync=True, changelistId=0):
    """
	:param filepath: :class: str
	:param description: :class: str
	:param force: :class: bool
	:param doSync: :class: bool
	:param changelistId: :class: int
	:return: :class: perforce.data.Changelist
	"""

    if not isInP4(filepath):
        if not os.path.exists(filepath):
            raise Exception('Critical Error: File - %s - does not exist on the local file system.' % filepath)

    changelist = None
    if changelistId == 0 and not description == 'default':
        if changelistExists(description):
            changelist = getChangelist(description)
        else:
            changelist = createChangelist(description)
    elif not description == 'default':
        if changelistWithIdExists(changelistId):
            changelist = getChangelistById(changelistId)
        else:
            changelist = createChangelist(description)

    instance = __getInstance()
    if isInP4(filepath):
        if isDeleted(filepath):
            return restore(filepath, changelist, changelistId)

    if not isInP4(filepath):
        if changelist == None:
            instance.run('add', filepath)
            return p4Data.Changelist.getDefaultChangelist(client=instance.client, user=instance.user)
        else:
            instance.run('add', '-c%s' % changelist.change, filepath)

    if not isCheckedOutByCurrentUser(filepath):
        if not isLatest(filepath):
            if doSync == True:
                sync(filepath, force=force)

        if changelist == None:
            instance.run('edit', filepath)
        else:
            instance.run('edit', '-c%s' % changelist.change, filepath)

        return p4Data.Changelist.getDefaultChangelist(client=instance.client,
                                                      user=instance.user) if changelist is None else changelist


def changelistWithIdExists(changelistId):
    changelists = getPendingChangelists()

    if isinstance(changelists, list):
        for changelist in changelists:
            if changelistId == changelist.change:
                return True
    return False


def createChangelist(description='Updated via tools'):
    if changelistExists(description): return getChangelist(description)
    instance = __getInstance()

    change = {}
    change['Description'] = str(description)
    change['Change'] = 'new'
    instance.input = change
    result = instance.run('change', '-i')[0]
    instance.input = ''
    changelistId = result[result.find(' ') + 1:result.rfind(' ')]
    return getChangelistById(changelistId)


def describeChangelist(changelistId):
    return p4Data.ChangelistDescription(__getInstance().run('describe', changelistId)[0])


def getChangelistById(changelistId):
    """
    :param changelistId: :class: str'
    :return: :class: toolShed.services.perforce.data.Changelist
    """
    instance = __getInstance()
    if changelistId == 'default':
        return p4Data.Changelist.getDefaultChangelist(client=instance.client, user=instance.user)

    changelists = getPendingChangelists()
    if isinstance(changelists, list):
        for changelist in changelists:
            if changelistId == changelist.change:
                return changelist

    raise Exception('Changelist with id - %s - does not exist.' % changelistId)


def getChangelist(description):
    """
	:param description: :class: str
	:return: :class: toolShed.services.perforce.data.Changelist
	"""
    instance = __getInstance()
    if description == 'default':
        return p4Data.Changelist.getDefaultChangelist(client=instance.client, user=instance.user)

    changelists = getPendingChangelists()
    descriptionCandidate = description.lower()

    if isinstance(changelists, list):
        for changelist in changelists:
            if descriptionCandidate == changelist.description.lower().rstrip():
                return changelist

    raise Exception('Changelist with description - %s - does not exist.' % description)


def changelistExists(description):
    """
	:param description: :class: str
	:return: :class: bool
	"""
    try:
        getChangelistNumber(description)
    except:
        return False
    return True


def getChangelistNumber(description):
    """
	:param description: :class: str
	:return: :class: str
	"""
    changelists = getPendingChangelists()
    
    descriptionCandidate = description.lower()

    if isinstance(changelists, list):
        for changelist in changelists:
            clDesc = changelist.description.lower().rstrip()
            
            if descriptionCandidate == clDesc:
                return changelist.change

    raise Exception('Changelist with description - %s - does not exist.' % description)


def getPendingChangelistId(filepath):
    """
	:param filepath: :class: str
	:return: :class: str
	"""
    filepath = filepath.replace('\\', '/')
    pendingFiles = getPendingFiles()
    for pendingFile in pendingFiles:
        depotToClientPath = getClientFilepath(pendingFile.depotFile).replace('\\', '/')
        if filepath == depotToClientPath:
            return 'default' if pendingFile.change == None else pendingFile.change


def getPendingFile(filepath):
    """
	:param filepath: :class: str
	:return: :class: toolShed.services.perforce.data.PendingFile
	"""
    filepath = filepath.replace('\\', '/')
    pendingFiles = getPendingFiles()
    for pendingFile in pendingFiles:
        depotToClientPath = getClientFilepath(pendingFile.depotFile).replace('\\', '/')
        if depotToClientPath == filepath:
            return pendingFile

    raise Exception('Could not resolve %s into Perforce file data.' % filepath)


def getPendingFiles():
    """
	:return: :class: list of :class: toolShed.services.perforce.data.PendingFile
	"""
    instance = __getInstance()
    datas = instance.run('opened', '-u%s' % instance.user, '-C%s' % instance.client)
    return [p4Data.PendingFile(data=data) for data in datas]


def getPendingChangelists():
    """
	:return: :class: toolShed.services.perforce.data.Changelist
	"""
    instance = __getInstance()
    info = instance.run('info')[0]
    command = 'changes', '-s%s' % 'pending', '-u%s' % getpass.getuser(), '-c%s' % info['clientName']
    items = instance.run(command)
    return [p4Data.Changelist(data=item) for item in items]


def isDeleted(filepath):
    """
	:param filepath: :class: str
	:return: :class: bool
	"""
    if not isInP4(filepath):
        return False
    instance = __getInstance()
    result = instance.run('files', filepath)[0]
    return True if result['action'] == 'delete' or result['action'] == 'move/delete' else False


def isInClientView(filepath):
    """
	:param filepath: :class: str
	:return: :class: bool
	"""
    instance = __getInstance()
    try:
        info = instance.run('files', filepath.replace('\\', '/'))
        return True
    except Exception as error:
        if 'no such file' in str(error):
            return True
        if "is not under client's root" in str(error):
            return False


def isInP4(filepath):
    """
	:param filepath: :class: str
	:return: :class: bool
	"""
    instance = __getInstance()
    try:
        info = instance.run('files', filepath.replace('\\', '/'))
        return True if not info is None else False
    except Exception as error:
        if 'no such file' in str(error):
            return False
        if 'An empty string is not allowed as a file name' in str(error):
            return False
        if "is not under client's root" in str(error):
            return False
        raise Exception(error)


def getUsersWithCheckedOutFile(filepath, includeCurrentUser=True):
    """
	:param filepath: :class: str
	:param includeCurrentUser: :class: bool
	:return: :class: list of :class: str
	"""
    instance = __getInstance()
    currentUser = getpass.getuser()
    userNames = []
    try:
        stats = instance.run('opened', "-a", filepath)
        for stat in stats:
            if 'user' in stat:
                userNames.append(stat['user'])

    except Exception as error:
        if 'no such file' in str(error):
            return userNames
        if 'An empty string is not allowed as a file name' in str(error):
            return userNames
        if "is not under client's root" in str(error):
            return userNames
        raise Exception(error)

    if includeCurrentUser == False:
        if currentUser in userNames:
            userNames.remove(currentUser)

    return userNames


def isCheckedOutByAnyoneElse(filepath):
    """
	:param filepath: :class: str
	:return: :class: bool
	"""
    instance = __getInstance()
    currentUser = getpass.getuser()
    try:
        stats = instance.run('opened', "-a", filepath)
        for stat in stats:
            if 'user' in stat:
                if stat['user'] != currentUser:
                    return True
    except Exception as error:
        if 'no such file' in str(error):
            return False
        if 'An empty string is not allowed as a file name' in str(error):
            return False
        if "is not under client's root" in str(error):
            return False
        raise Exception(error)
    return False


def isCheckedOutByCurrentUser(filepath):
    """
	:param filepath: :class: str
	:return: :class: bool
	"""
    instance = __getInstance()
    currentUser = getpass.getuser()
    try:
        stats = instance.run('opened', "-a", filepath)
        for stat in stats:
            if 'user' in stat:
                if stat['user'] == currentUser:
                    return True

    except Exception as error:
        if 'no such file' in str(error):
            return False
        if 'An empty string is not allowed as a file name' in str(error):
            return False
        if "is not under client's root" in str(error):
            return False
        raise Exception(error)
    return False


def isLatest(filepath):
    """
	:param filepath: :class: str
	:return: :class: bool
	"""
    instance = __getInstance()
    if not isInP4(filepath):
        raise Exception('File not in Perforce - %s' % filepath)

    fileStatDictionaries = instance.run('fstat', filepath)

    if fileStatDictionaries is None or len(fileStatDictionaries) == 0:
        raise Exception('Not able to evaluate if "%s" is latest version for unknown reason' % filepath)

    fileStatDictionary = fileStatDictionaries[0]
    if 'haveRev' in fileStatDictionary.keys() and 'headRev' in fileStatDictionary.keys():
        haveRevision = fileStatDictionary['haveRev']
        headRevision = fileStatDictionary['headRev']
        return True if haveRevision == headRevision else False

    return False


def isLocked(filepath):
    """
	:param filepath: :class: str
	:return: :class: bool
	"""
    if isCheckedOutByCurrentUser(filepath):
        pendingFile = getPendingFile(filepath)
        return pendingFile.ourLock

    else:
        instance = __getInstance()
        fileStatDictionaries = instance.run('fstat', filepath)
        if fileStatDictionaries is None or len(fileStatDictionaries) == 0:
            raise Exception('Not able to evaluate if "%s" is latest version for unknown reason' % filepath)
        fileStatDictionary = fileStatDictionaries[0]
        return True if 'otherLocks' in fileStatDictionary.keys() else False


def isExlusivelyCheckedOut(filepath):
    """
	:param filepath: :class: str
	:return: :class: bool
	"""
    instance = __getInstance()
    fileStatDictionaries = instance.run('fstat', filepath)
    if fileStatDictionaries is None or len(fileStatDictionaries) == 0:
        raise Exception('Not able to evaluate if "%s" is latest version for unknown reason' % filepath)
    fileStatDictionary = fileStatDictionaries[0]
    if 'headType' in fileStatDictionary.keys():
        return True if re.search('\+l', fileStatDictionary['headType']) else False


def lockFile(filepath):
    """
	:param filepath: :class: str
	:return: None
	"""
    if not isCheckedOutByCurrentUser(filepath):
        raise Exception('File can not be locked because it is not checked out - %s' % filepath)
    if isLocked(filepath):
        return
    instance = __getInstance()
    instance.run('lock', filepath)


def markForDelete(filepath, description='Marked for delete via tools', force=False, doSync=True,
                  changelistId='default'):
    """
	:param filepath: :class: str
	:param description: :class: str
	:param force: :class: bool
	:param doSync: :class: bool
	:param changelistId: :class: str
	:return: :class: str
	"""
    if changelistId == 0 and changelistExists(description):
        changelistId = getChangelist(description).change

    if not isInP4(filepath):
        raise Exception('Cannot delete file that is not in Perforce - %s' % filepath)

    if isDeleted(filepath):
        raise Exception('Cannot delete file that is already deleted')

    if isCheckedOutByCurrentUser(filepath):
        raise Exception('Cannot delete file that is checked out on the local client')

    if isExlusivelyCheckedOut(filepath):
        raise Exception('Cannot delete file that is exclusively checked out by someone else')

    if not isLatest(filepath):
        if doSync == True:
            sync(filepath, force=force)

    if changelistId == 0:
        changelistId = createChangelist(description).change
    instance = __getInstance()
    instance.run('delete', '-c%s' % changelistId, filepath)
    return changelistId


@errorHandler
def unlockFile(filepath):
    """
	:param filepath: :class: str
	:return: None
	"""
    if not isCheckedOutByCurrentUser(filepath):
        raise Exception('File can not be locked because it is not checked out - %s' % filepath)
    if not isLocked(filepath):
        return
    instance = __getInstance()
    instance.run('unlock', filepath)


def lockChangelist(changelistId):
    """
	:param changelistId: :class: str
	:return: None
	"""
    instance = __getInstance()
    instance.run('lock', '-c%s' % changelistId)


def unlockChangelist(changelistId):
    """
	:param changelistId: :class: str
	:return: None
	"""
    instance = __getInstance()
    instance.run('unlock', '-c%s' % changelistId)


def sync(filepath, force=False):
    """
	:param filepath: :class: str
	:param force: :class: bool
	:return: None
	"""
    instance = __getInstance()
    try:
        if force == True:
            instance.run('sync', '-f', filepath)
        else:
            if not isLatest(filepath):
                instance.run('sync', filepath)
    except Exception as error:
        if 'Warning' in str(error) and 'file(s) up-to-date' in str(error):
            return
        raise Exception(str(error))


if __name__ == "__main__":  # Testing

    filepath = r'E:\depot\kraken_sculpin\tools\ToolShed\python\toolShed\dev\p4Test.txt'
# filepath = 'E:/depot/kraken_sculpin/source_art/Objects/Weapons/Generic/Generic_Sword.ma'
# description = 'Updated via tools'
# print isLocked(filepath)
# print isCheckedOutByCurrentUser(filepath)
# instance = __getInstance()
# info = instance.run('fstat', filepath)
# print info

# data = instance.run('opened', '-u%s' % instance.user, '-C%s' % instance.client)[1]
# for key, value in data.iteritems():
# 	print "'%s': '%s'," % (key, value)

# changelist = restore(filepath, description)
# changelist = checkOut(filepath, description)
# print changelist
# depotFilepath = getDepotFilepath(filepath)
# print depotFilepath
