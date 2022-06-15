class PendingFile(object):
	def __init__(self, data):
		"""
		:param data:  dict in the format:
		{
		'haveRev': '7',
		'rev': '7',
		'clientFile': '//akesso_SAN15-workLaptop/tools/ToolShed/python/toolShed/dev/p4Test.txt',
		'client': 'akesso_SAN15-workLaptop',
		'user': 'akesso',
		'action': 'edit',
		'type': 'text',
		'depotFile': '//kraken-sculpin/kraken-sculpin-mainline/tools/ToolShed/python/toolShed/dev/p4Test.txt',
		'change': 'default' or '479945'
		}
		"""
		super(PendingFile, self).__init__()
		self.__haveRevision = -1 if data['haveRev'] == 'none' else int(data['haveRev'])
		self.__revision = int(data['rev'])
		self.__clientFile = data['clientFile']
		self.__client = data['client']
		self.__user = data['user']
		self.__action = data['action']
		self.__type = data['type']
		self.__depotFile = data['depotFile']
		self.__change = data['change']
		self.__ourLock = True if 'ourLock' in data.keys() else False

	@property
	def action(self):
		"""
		:return:  str
		"""
		return self.__action


	@property
	def change(self):
		"""
		:return:  str
		"""
		return self.__change


	@property
	def client(self):
		"""
		:return:  str
		"""
		return self.__client


	@property
	def clientFile(self):
		"""
		:return:  str
		"""
		return self.__clientFile


	@property
	def depotFile(self):
		"""
		:return:  str
		"""
		return self.__depotFile


	@property
	def haveRevision(self):
		"""
		:return:  int
		"""
		return self.__haveRevision


	@property
	def ourLock(self):
		"""
		:return:  bool
		"""
		return self.__ourLock


	@property
	def revision(self):
		"""
		:return:  int
		"""
		return self.__revision


	@property
	def type(self):
		"""
		:return:  str
		"""
		return self.__type


	@property
	def user(self):
		"""
		:return:  str
		"""
		return self.__user


class ChangelistDescription(object):
	def __init__(self, data):
		"""
		:param data:  dict in the format:
		{
		'status': 'submitted',
		'fileSize': ['149972', '332412', '228164'],
		'changeType': 'public',
		'rev': ['30', '9', '2'],
		'client': 'sdeprie_SAN-HGS2RG1_9791',
		'user': 'sdeprie',
		'oldChange': '479526',
		'time': '1505781931',
		'action': ['edit', 'edit', 'edit']',
		'path': '//kraken-sculpin/kraken-sculpin-mainline/game/projects/Client/...',
		'digest': ['3D5F653AC1DBE2524BEEDE6D90FB16BE', '6EAFED0E1948427399CBC3C784B318CA', '9B3E678AED22B8563C89FE40D4897BB6'],
		'type': ['binary+lm', 'text', 'text']',
		'depotFile': ['//kraken-sculpin/kraken-sculpin-mainline/game/projects/Client/Levels/ClientStartupLevel/ClientStartupLevel.cry', '//kraken-sculpin/kraken-sculpin-mainline/game/projects/Client/Slices/BlockASaurus_001.slice', '//kraken-sculpin/kraken-sculpin-mainline/game/projects/Client/Slices/BlockASaurus_Big_001.slice'],
		'change': '479785',
		'desc': 'It came down to the physics node. It was destroying everything (the out of skin experience, the double meshes, the failure to move).  I nuked it and added it again, as it's needed for character movement.'
		}
		"""
		super(ChangelistDescription, self).__init__()
		self.__status = data['status']
		self.__filesize = [int(value) for value in data['fileSize']]
		self.__changeType = data['changeType']
		self.__revision = [int(value) for value in data['rev']]
		self.__client = data['client']
		self.__user = data['user']
		self.__time = int(data['time'])
		self.__action = data['action']
		self.__path = data['path']
		self.__digest = data['digest']
		self.__type = data['type']
		self.__depotFile = data['depotFile']
		self.__change = int(data['change'])
		self.__description = data['desc']

	@property
	def action(self):
		"""
		:return:  str
		"""
		return self.__action


	@property
	def change(self):
		"""
		:return:  int
		"""
		return self.__change


	@property
	def changeType(self):
		"""
		:return:  str
		"""
		return self.__changeType


	@property
	def client(self):
		"""
		:return:  str
		"""
		return self.__client


	@property
	def depotFile(self):
		"""
		:return:  str
		"""
		return self.__depotFile


	@property
	def description(self):
		"""
		:return:  str
		"""
		return self.__description


	@property
	def digest(self):
		"""
		:return:  str
		"""
		return self.__digest


	@property
	def filesize(self):
		"""
		:return:  int
		"""
		return self.__filesize


	@property
	def path(self):
		"""
		:return:  str
		"""
		return self.__path


	@property
	def revision(self):
		"""
		:return:  int
		"""
		return self.__revision


	@property
	def status(self):
		"""
		:return:  str
		"""
		return self.__status


	@property
	def time(self):
		"""
		:return:  int
		"""
		return self.__time


	@property
	def type(self):
		"""
		:return:  str
		"""
		return self.__type


	@property
	def user(self):
		"""
		:return:  str
		"""
		return self.__user

class RevisionHistory(object):
	def __init__(self, data):
		"""
		:param data:  dict in the following format
		{
			'fileSize':[None, '10'],
			'rev':['2', '1'],
			'client': ['akesso_SAN15-work', 'akesso_SAN15-work'],
			'user': ['akesso', 'akesso'],
			'time': ['1503346178', '1503100737'],
			'action': ['delete', 'add'],
			'digest': ['None', '617185C30114C1AF3BC48160322C4AAF'],
			'type':['text', 'text'],
			'depotFile': '//kraken-sculpin/kraken-sculpin-mainline/source_art/Objects/Weapons/ChainBlade/Animation/ChainBlade_Idle_02.ma',
			'change':['462395', '461973'],
			'desc':['Delete via tools', 'Added']
		}
		"""
		super(RevisionHistory, self).__init__()

		previousItem = None
		self.__items = []
		for i in reversed ( range(len(data['fileSize'])) ):

			item = RevisionHistoryItem(
										owner = self,
										filesize=int(data['fileSize'][i]) if not data['fileSize'][i] == None else 0,
										revision=int(data['rev'][i]),
										client=data['client'][i],
										user=data['user'][i],
										time=int(data['time'][i]),
										action=data['action'][i],
										digest=data['digest'][i],
										fileType=data['type'][i],
										change=int(data['change'][i]),
										description=data['desc'][i],
										previousRevision=previousItem
										)
			self.__items.append(item)
			previousItem = item

		self.__depotFile = data['depotFile']

	@property
	def items(self):
		"""
		:return:  list of  toolShed.services.perforce.data.RevisionHistoryItems instances
		"""
		return self.__items

	@property
	def depotFile(self):
		"""
		:return:  str
		"""
		return self.__depotFile


class RevisionHistoryItem(object):

	def __init__(self, owner, filesize, revision, client, user, time, action, digest, fileType, change, description, previousRevision=None):
		"""
		:param owner:  toolShed.services.perforce.data.RevisionHistory
		:param filesize:  int
		:param revision:  int
		:param client:  str
		:param user:  str
		:param time:  int
		:param action:  str
		:param digest:  str
		:param fileType:  str
		:param change:  int
		:param description:  str
		:param previousRevision:  toolShed.services.perforce.data.RevisionHistory
		"""
		super(RevisionHistoryItem, self).__init__()
		self.__owner = owner
		self.__filesize = filesize
		self.__revision = revision
		self.__client = client
		self.__user = user
		self.__time = time
		self.__action = action
		self.__digest = digest
		self.__fileType = fileType
		self.__change = change
		self.__description = description
		self.__previousRevision = previousRevision

	@property
	def owner(self):
		"""
		:return:  toolShed.services.perforce.data.RevisionHistory 
		"""
		return self.__owner

	@property
	def previousRevision(self):
		"""
		:return:  toolShed.services.perforce.data.RevisionHistoryItem
		"""
		return self.__previousRevision

	@property
	def filesize(self):
		"""
		:return:  int
		"""
		return self.__filesize

	@property
	def revision(self):
		"""
		:return:  int
		"""
		return self.__revision

	@property
	def client(self):
		"""
		:return:  str
		"""
		return self.__client

	@property
	def user(self):
		"""
		:return:  str
		"""
		return self.__user

	@property
	def time(self):
		"""
		:return:  int
		"""
		return self.__time

	@property
	def action(self):
		"""
		:return:  str
		"""
		return self.__action

	@property
	def digest(self):
		"""
		:return:  str
		"""
		return self.__digest

	@property
	def fileType(self):
		"""
		:return:  str
		"""
		return self.__fileType

	@property
	def change(self):
		"""
		:return:  int
		"""
		return self.__change

	@property
	def description(self):
		"""
		:return:  str
		"""
		return self.__description



class Changelist(object):

	@staticmethod
	def getDefaultChangelist(client, user):
		"""
		:param client:  str
		:param user:  str
		:return:  toolShed.services.perforce.data.Changelist
		"""
		data = {}
		data['client'] = client
		data['user'] = user
		data['status'] = 'pending'
		data['changeType'] = 'public'
		data['change'] = 'default'
		data['desc'] = 'default'
		return Changelist(data=data)

	def __init__(self, data):
		"""
		:param data:  dict in the following format
		{
			'status': 'pending',
			'changeType': 'public',
			'client': 'the workspace name',
			'user': 'the user name',
			'time': '1503346178',
			'change':'462395',
			'desc': 'The Description'
		}
		"""
		super(Changelist, self).__init__()
		self.__status = '' if not 'status' in data.keys() else data['status']
		self.__changeType = '' if not 'changeType' in data.keys() else data['changeType']
		self.__client = '' if not 'client' in data.keys() else data['client']
		self.__user = '' if not 'user' in data.keys() else data['user']
		self.__time = -1 if not 'time' in data.keys() else data['time']
		self.__change = '' if not 'change' in data.keys() else data['change']
		self.__description = '' if not 'desc' in data.keys() else data['desc'].rstrip()

	def __str__(self):
		return """toolShed.services.perforce.data.Changelist
		status=%s
		changeType=%s
		client=%s
		user=%s
		time=%s
		id=%s
		description=%s
		""" % (self.status, self.changeType, self.client, self.user, self.time, self.change, self.description)

	@property
	def status(self):
		"""
		:return:  str
		"""
		return self.__status

	@property
	def changeType(self):
		"""
		:return:  str
		"""
		return self.__changeType

	@property
	def client(self):
		"""
		:return:  str
		"""
		return self.__client

	@property
	def user(self):
		"""
		:return:  str
		"""
		return self.__user

	@property
	def time(self):
		"""
		:return:  str
		"""
		return self.__time

	@property
	def change(self):
		"""
		:return:  str
		"""
		return self.__change

	@property
	def description(self):
		"""
		:return:  str
		"""
		return self.__description