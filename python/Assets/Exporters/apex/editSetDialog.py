import pymel.core as pm
from pymel.core.system import Path
import os as os
import Assets
import re


class editSetDialog(object):

    windowName = "Dex Asset Parameters"
       

    window = None
    instance = None

    setInstance = None
 
    def __init__(self, mySet):
        editSetDialog.instance = self
        
        self.setInstance = mySet
        self.customAssetWidget = None
                
        if pm.window(editSetDialog.windowName, exists=True):
            pm.deleteUI(editSetDialog.windowName)

        if pm.windowPref( editSetDialog.windowName, exists=True):
            pm.windowPref( editSetDialog.windowName, remove=True)

        with pm.window(editSetDialog.windowName, title="Edit Set", width=400, height=150, sizeable=True) as self.window:
                        
            with pm.columnLayout(adjustableColumn=True) as self.mainCol:
                self.folderGrp = pm.textFieldButtonGrp( label='Export Folder', 
                    text=mySet.ExportLocation.get(), 
                    buttonLabel='Browse', 
                    adjustableColumn=2,
                    buttonCommand=self._browseForFolder,
                    textChangedCommand=self._updateSet
                    )

                self.filenameText = pm.textFieldGrp( label='Export Filename', 
                    text=mySet.ExportFilename.get(),
                    adjustableColumn=2,
                    textChangedCommand=self._updateSet
                    )

                self.exportTypeMenu = pm.optionMenuGrp(label='Export Type', changeCommand=self._updateSet)

                for i in Assets.assetTypes.keys():
                    pm.menuItem( label=i )

                self.exportTypeMenu.setValue( mySet.AssetType.get() )

                self._updateCustomAssetWidget()

        self.window.show()   

    def _updateCustomAssetWidget(self):
        if (self.customAssetWidget != None):
            pm.deleteUI(self.customAssetWidget)

        print "* UpdateCustomAssetWidget"
        
        assetHandler = Assets.GetHandlerForSet(self.setInstance)
        self.customAssetWidget = assetHandler.DrawCustomUI(self.mainCol)

    def _browseForFolder(self, *args):
        exportLocation = self.setInstance.ExportLocation.get()
        
        scene = pm.sceneName()  # Result: Path('D:/Dante/geo/bell_b.ma') #     
        if scene == "":
            msg = "Dex works with relative paths, so you will have to save the scene before you can choose an export location.  Sorry for the inconvenience!"
            pm.confirmDialog(title="Please save the Scene", message=msg)
        else:
            sceneDir = os.path.dirname(scene)  # Result: u'D:/Dante/geo' #

            startFolder = ""

            if exportLocation == "":
                exportLocation = "."
            
            if exportLocation[0] == ".":        
                startFolder = (sceneDir + "/" + exportLocation)
            else:
                startFolder = exportLocation

    
            returnFileList = pm.fileDialog2(fileMode=2, startingDirectory=startFolder)
            
            if returnFileList is not None:
                if returnFileList[0] is not None:
                    #print( "Returned File Results: " + returnFileList[0])

                    sceneDriveLetter = scene[0:2]
                    exportDriveLetter = returnFileList[0][0:2]
                    #print( "Returned File DriveLetter: " + exportDriveLetter)
                    #print( "Returned Scene DriveLetter: " + sceneDriveLetter)

                    if sceneDriveLetter == exportDriveLetter:
                        print("We're on the same drive!")
                        exportFolder = os.path.normpath(returnFileList[0])
                        exportFolder = "./" + os.path.relpath(exportFolder, sceneDir)
                    else:
                        print("We're on different drives!")
                        exportFolder = returnFileList[0]

                    self.folderGrp.setText(exportFolder)

    #@staticmethod
    def _updateSet(self, *args, **kwargs):
        self.setInstance.ExportLocation.set(self.folderGrp.getText())
        self.setInstance.ExportFilename.set(self.filenameText.getText())

        AssetTypeText = self.exportTypeMenu.getValue()

        prevAssetType = self.setInstance.AssetType.get()
        
        newName = self.filenameText.getText()
        parts = newName.split('.')
        newName = parts[0] + "_EXPORT"
        
        #these shenanigans are to trigger the ui to update from the rename.
        #renaming it to a bogus name first lets us update teh UI even when it's only the folder that changed
        #TODO: This should probably be re-workded
        self.setInstance.rename(newName + "a")  
        self.setInstance.rename(newName)

        

        if prevAssetType != AssetTypeText:
            print(prevAssetType + " is not the same as " + AssetTypeText )
            self.setInstance.AssetType.unlock()
            self.setInstance.AssetType.set(AssetTypeText)
            self.setInstance.AssetType.lock()

            #TODO: Trigger the editSetDialog to remove and re-draw the DrawCustomUI part
            self._updateCustomAssetWidget()

            #TODO: Probably wan tto move this to the parent class of Assets
            assetHandler = Assets.GetHandlerForSet(self.setInstance)
            assetHandler.InitializeSet()