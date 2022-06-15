verbose = True
if verbose: print("> baseAsset loading")

import Assets
import pymel.core as pm
import os
import lib.maya.FBXSettings as FBXSettings
reload(FBXSettings)

#from lib.perforce import client as p4
#reload(p4)


class SaveBeforeScene(object):
    def __init__(self):
        if verbose: print "SaveBeforeScene constructor"
        super(SaveBeforeScene, self).__init__()


class baseAsset(object):
    stringId = "baseAsset" 

    def __init__(self, exportSet):
        if verbose: print "baseAsset constructor"
        self.set = exportSet
        self.stringId = "baseAsset"
        self.data = dict()
        self.settings = FBXSettings.NewSettings()

        self.Tasks = list()

        self.saveBeforeExport = True
        self.checkOutBeforeExport = True
        self.addAfterExport = True

    def InitializeSet(self):
        if verbose: print("--> base asset InitializeSet")

    def add(self, theFile, description=None):
        try:
            if verbose: print("File Add: " + theFile)
            if not p4.isInP4(theFile):               
                if description is None:
                    if verbose: print("** using default description **")
                    description = self.GetAssetDescription()

                if len(description) > 31:
                    if verbose: print("Warning:  Description was longer than 31 characters, truncating!")
                    description = description[0:31]

                if p4.changelistExists(description) is False:   
                    if verbose: print("Add Changelist '{0} did not exist,creating it ".format(description))
                    p4.add(theFile, description)
                else:
                    CL = p4.getChangelist(description)
                    if verbose: print("Add Changelist '{0}' found, CL.change is: {0}".format(description, CL.change))
                    p4.add(theFile, description, changelistId=CL.change)
            else:
                print("File already in an open changelist.")


        except Exception as error:
            error = str(error)
            print("WARNING: Perforce encountered this error: \n%s" % error)

    def checkout(self, theFile, description=None):
        try:
            if verbose: print("File Checkout: " + theFile)
            if p4.isInP4(theFile):
                if not p4.isCheckedOutByCurrentUser(theFile):
                
                    print("File Edit: " + theFile)
                    
                    if description is None:
                        if verbose: print("** using default description **")
                        description = self.GetAssetDescription()

                    if len(description) > 31:
                        if verbose: print("Warning:  Description was longer than 31 characters, truncating!")
                        description = description[0:31]

                    if p4.changelistExists(description) is False:   
                        if verbose: print("Edit Changelist '{0} did not exist,creating it ".format(description))
                        p4.checkOut(theFile, description)
                    else:
                        CL = p4.getChangelist(description)
                        if verbose: print("Edit Changelist '{0}' found, CL.change is: {0}".format(description, CL.change))
                        p4.checkOut(theFile, description, changelistId=CL.change)
                else:
                    print("File already checked out.")

        except Exception as error:
            error = str(error)
            print("WARNING: Perforce encountered an error: \n%s" % error)

    def GetAssetDescription(self):
        """
        This is currently used for the perforce changelist
        """
        sc = pm.sceneName()  # Result: Path('D:/Dante/geo/bell_b.ma') #
        sc = os.path.basename(sc)  # Result: u'bell_b.ma' #
                
        return sc

    def GetOutputFile(self):
        ss = Assets.GetSceneSettings()
        sceneLoc = ss.ExportLocation.get()

        loc = self.set.ExportLocation.get()
        locFile = self.set.ExportFilename.get()

        finalLoc = sceneLoc + "/" + loc + "/" + locFile
        finalLoc = Assets.toLocalPath(finalLoc)

        return finalLoc

    def GetOutputFolder(self):

        loc = self.set.ExportLocation.get()

        loc = loc
        loc = Assets.toLocalPath(loc)

        return loc

    def GetSelectionToExport(self):
        pm.select(self.set.members())
        
    def ValidateForExport(self):
        valid = False

        if len(self.set.members()) > 0:
            valid = True
        else:
            raise Exception(self.set.nodeName() + " is empty - I cannot export nothing!")

        return valid

    def SetFBXOptions(self):
        if verbose: print("--> base asset is setting FBX options!")
                
        pm.mel.eval('FBXResetExport')  # because pm.FBXResetExport() doesn't seem to do the trick!  #todo @ahogan find out if this is still true

        self.settings['Import|AdvOptGrp|UI|GenerateLogData']['VALUE'] = "false"   #appears to have little to no effect

        self.settings['Export|AdvOptGrp|Fbx|AsciiFbx']['VALUE'] = "ASCII"
        self.settings['Export|AdvOptGrp|AxisConvGrp|UpAxis']['VALUE'] = "Y"
        self.settings['Export|AdvOptGrp|Fbx|ExportFileVersion']['VALUE'] = "FBX201600"
        self.settings['Export|AdvOptGrp|UnitsGrp|UnitsSelector']['VALUE'] = "Millimeters"

    def ApplyFBXOptions(self):
        # We apply th FBX options as a second step to give derived asset handlers the chance to override or
        # append to the FBXSettings before they are applied.
        if verbose: print("--> base asset is applying FBX settings")
        self.settings = FBXSettings.FBXSettings

        for s in self.settings.keys():
            valueContainer = ""

            if self.settings[s]["TYPE"] == "Enum":
                valueContainer = '"'

            command = 'FBXProperty {0} -v {2}{1}{2}'.format(self.settings[s]['PATH'], self.settings[s]['VALUE'],
                                                            valueContainer)
            if verbose: print ('  --->' + command)

            pm.mel.eval(command)

    def PreExport(self):
        if verbose: print("--> base asset pre export step!")

        """ if self.checkOutBeforeExport:
            file = self.GetOutputFile()
            self.checkout(file)

            sourceFile = pm.sceneName()
            if sourceFile != "" and sourceFile != None:
                self.checkout(sourceFile) """

        if self.saveBeforeExport:
            try:
                pm.saveFile()
            except BaseException as error:
                error = str(error)
                print("WARNING: Couldn't save file: \n%s" % error)

    def Export(self):
        if verbose: print("--> base asset export step!")

        loc = self.GetOutputFile()

        if verbose: print("--> base asset exporting to " + loc)

        folder = os.path.dirname(loc)

        if verbose: print("--> base asset checking/creating " + folder)
        if not os.path.exists(folder):
            os.makedirs(folder)

        self.GetSelectionToExport()

        try:
            exportCommand = 'FBXExport -f "{0}" -s'.format(loc)
            print("Exporting: \t" + loc)
            print("CMD: " + exportCommand)
            pm.mel.eval('FBXExportGenerateLog -v false;')
            pm.mel.eval(exportCommand)
            print("Export Succeeded:\t" + loc + "\n") 
        except:
            print("Export Failed:\t" + loc + "\n")

    def PostExport(self):
        if verbose: print("--> base asset post export step!")

        """ if self.addAfterExport:
            file = self.GetOutputFile()
            self.add(file)

            sourceFile = pm.sceneName()

            if sourceFile != "" and sourceFile != None:
                self.add(sourceFile, self.GetAssetDescription()) """
    
    def DrawCustomUI(self, parentControl):
        if verbose: print("--> base asset DrawCustomUI")
        #Override this function in your inherited classes to allow for your custom UI module to be added into editors
        return None
