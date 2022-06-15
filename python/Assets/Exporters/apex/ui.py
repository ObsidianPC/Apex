verbose = False
import pymel.core as pm
import Settings
import subprocess
import os
import maya.OpenMaya as om
import lib.pyperclip as pyperclip


import Assets
reload(Assets)

import lib.maya.events as events
reload(events)

import editSetDialog as esd
reload(esd)

import apexSetList as setListWidget
reload(setListWidget)

"""This class builds a ui to handle exporting set contents to FBX.  Only one instance is allowed, so
we'll have a mostly static set of data and spawn a UI that uses that."""

windowName = "Apex"
window = None
exportSets = list()
ui_assetLabelStyle = 4
ui_setList = None
ui_SceneFolderGrp = None


uiDeletedCallbackID = "apex_uiDeletedCallbackID"
uiSetAddedCallbackID = "apex_uiSetAddedCallbackID"
uiSetRemovedCallbackID = "apex_uiSetRemovedCallbackID"
uiSetChangedCallbackID = "apex_uiSetChangedCallbackID"
idleEventID = "apex_idleEventID"

userEvent_setsChanged = "apex_setsChanged"
nodeRenamed_callbackID = "apex_nodeRenamed"



eventManager = events.eventManager()
iconpath = r"python/Assets/Exporters/apex/icons"

ICON_CreateOneAssetForSelected = r"{0}/{1}/CreateOneAssetForSelected.png".format(Settings.ARTTOOL_ROOT.value,
                                                                                 iconpath)
ICON_CreateAssetForEachSelected = r"{0}/{1}/CreateAssetForEachSelected.png".format(Settings.ARTTOOL_ROOT.value,
                                                                                   iconpath)
ICON_EditAsset = r"{0}/{1}/EditAsset.png".format(Settings.ARTTOOL_ROOT.value, iconpath)
ICON_DeleteAsset = r"{0}/{1}/DeleteAsset.png".format(Settings.ARTTOOL_ROOT.value, iconpath)
ICON_ExportAll = r"{0}/{1}/ExportAll.png".format(Settings.ARTTOOL_ROOT.value, iconpath)

ICON_AddToAsset = r"{0}/{1}/AddToAsset.png".format(Settings.ARTTOOL_ROOT.value, iconpath)
ICON_RemoveFromAsset = r"{0}/{1}/RemoveFromAsset.png".format(Settings.ARTTOOL_ROOT.value, iconpath)
ICON_ExportAsset = r"{0}/{1}/ExportAsset.png".format(Settings.ARTTOOL_ROOT.value, iconpath)

POPUP = None

def create():
    global ui_setList
    global ui_SceneFolderGrp
    global POPUP

    if pm.window(windowName, exists=True):
        pm.deleteUI(windowName)

    if pm.windowPref(windowName, exists=True):
        pm.windowPref(windowName, remove=True)

    with pm.window(windowName, title=windowName, width=250, height=650, sizeable=True) as window:

        with pm.formLayout(numberOfDivisions=100) as form:
            with pm.rowLayout(numberOfColumns=5,
                              columnWidth5=[50, 50, 50, 50, 50],
                              columnAttach5=["both", "both", "both", "both", "both"],
                              adjustableColumn5=3,
                              columnAlign5=["center", "center", "center", "center", "center"]) as topButtonBar:
                pm.symbolButton(image=ICON_EditAsset, height=50, command=_editExportSet,
                                annotation="Edit selected Asset")

                pm.text(label=" ")
                pm.text(label=" ")
                pm.symbolButton(image=ICON_CreateOneAssetForSelected, height=50, command=_createNewSet,
                                annotation="Create Asset")
                pm.symbolButton(image=ICON_CreateAssetForEachSelected, height=50, command=_createNewSetForEach,
                                annotation="Create Asset for Each")

            sceneSettings = Assets.GetSceneSettings()

            
            with pm.columnLayout(adjustableColumn=True) as sceneFolderBar:
                ui_SceneFolderGrp = pm.textFieldButtonGrp( label='Scene Export Folder', 
                    text=sceneSettings.ExportLocation.get(),
                    buttonLabel='Browse',
                    adjustableColumn3=2,
                    buttonCommand=_browseForSceneExportFolder
                    #textChangedCommand=self._updateSet
                    )
                

            ui_setList = setListWidget.createSetList()
            ui_setList.setAttachButtonRight(1)
            ui_setList.setSelectCommand(_onListSelectCommand)
            ui_setList.setPressCommand([(1, _addSelectionToSet),
                                        (2, _removeSelectionFromSet),
                                        (3, _exportSelectedSets)])

            ui_setList.setItemDoubleClickCommand2(_itemDoubleClickCommand2)

            ui_setList.customizeItemDelegate = _customizeListItem

            def popupPostCommand(*args):
                pm.popupMenu(POPUP, edit=True, deleteAllItems=True)

                selectedItems = ui_setList.getSelectedItems()
                if selectedItems is not None:
                    if ui_setList.isLeaf(selectedItems[0]):
                        pass
                    else:
                        pm.menuItem(label="Explore to FBX", parent=POPUP, command=exploreToFBX)
                        pm.menuItem(label="Copy FBX File Path(s) to Clipboard", parent=POPUP, command=copyFBXtoClipBoard)
                        pm.menuItem(label="Copy FBX Folder Path(s) to Clipboard", parent=POPUP, command=copyFoldertoClipBoard)
                        pm.menuItem(label="Show/Hide Asset in Outliner", parent=POPUP, command=toggleAssetOutlinerVisibility)


            POPUP = pm.popupMenu(parent=ui_setList.control, postMenuCommand=popupPostCommand)
            
            
            with pm.rowLayout(numberOfColumns=3,
                              columnWidth3=[50, 50, 50],
                              columnAttach3=["both", "both", "both"],
                              adjustableColumn3=2,
                              columnAlign3=["center", "center", "center"]) as bottomButtonBar:
                pm.symbolButton(image=ICON_DeleteAsset, height=50, command=_deleteSelectedExportSets,
                                annotation="Delete selected Assets")
                pm.text(label=" ")

                pm.symbolButton(image=ICON_ExportAll, height=50, command=_exportAllSets, annotation="Export All")

        pm.formLayout(form,
                      edit=True,
                      attachForm=[(topButtonBar, 'top', 5),
                                  (topButtonBar, 'left', 5),
                                  (topButtonBar, 'right', 5),

                                  (sceneFolderBar, 'left', 5),
                                  (sceneFolderBar, 'right', 5),

                                  (ui_setList.control, 'left', 5),
                                  (ui_setList.control, 'right', 5),

                                  (bottomButtonBar, 'left', 5),
                                  (bottomButtonBar, 'right', 5),
                                  (bottomButtonBar, 'bottom', 5),
                                  (bottomButtonBar, 'top', 95)],
                                  
                      attachControl=[(sceneFolderBar, 'top', 5, topButtonBar), 
                                    (ui_setList.control, 'top', 5, sceneFolderBar),
                                    (ui_setList.control, 'bottom', 5, bottomButtonBar)
                                    ],
                      attachNone=(bottomButtonBar, 'top')
                      )

    window.show()

    _refreshSetList()

    # set up callbacks
    eventManager.addUiDeletedCallback(window, uiDeletedCallbackID, uiDeleteCallback)
    #eventManager.addNodeAddedCallback(uiSetAddedCallbackID, uiSetAdded, strNodeType="objectSet")
    eventManager.addNodeRemovedCallback(uiSetRemovedCallbackID, nodeDeletedCallback)
    eventManager.registerUserEvent(userEvent_setsChanged, uiSetChangeDetected)
    #eventManager.registerNameChangedCallback(nodeRenamed_callbackID, _onNodeRenamed)


def _browseForSceneExportFolder(*args):
    global ui_SceneFolderGrp
    ss = Assets.GetSceneSettings()
    startFolder = ss.ExportLocation.get()

    returnFileList = pm.fileDialog2(fileMode=2, startingDirectory=startFolder)
    
    if returnFileList is not None:
        if returnFileList[0] is not None:
            
            exportFolder = os.path.normpath(returnFileList[0])
            
            ss.ExportLocation.set(exportFolder)
            ui_SceneFolderGrp.setText(exportFolder)


def _itemDoubleClickCommand2(item, itemDisplayLabel):
    if verbose: print("itemDoubleClickCommand2 with itemDisplayLabel={0} and item={1}".format(itemDisplayLabel, item))
    
    global ui_setList
    
    if ui_setList.isLeaf(item):
        parentItem = ui_setList.itemParent(item)
        objectSet = _getSetForItem(parentItem)
        
        matches = [o for o in objectSet if o.nodeName() == itemDisplayLabel]
        
        if len(matches) > 0:
            pm.select(matches[0])
    else:
        _editExportSet()

def _customizeListItem(item, parent=""):
    global ui_setList
    global ui_assetLabelStyle

    handler = None

    if parent is "":
        exportSet = Assets.GetAsset(item)

        if exportSet is not None:
            handler = Assets.GetHandlerForSet(exportSet)

        if handler is not None:
            ui_setList.setItemAnnotation(item, handler.GetOutputFile())

            ui_setList.setButtonImage(item, 1, ICON_AddToAsset)
            ui_setList.setButtonImage(item, 2, ICON_RemoveFromAsset)
            ui_setList.setButtonImage(item, 3, ICON_ExportAsset)

            ui_setList.setButtonTooltip(item, 1, "Add selected item(s) to this asset")
            ui_setList.setButtonTooltip(item, 2, "Remove selected item(s) from this asset")
            ui_setList.setButtonTooltip(item, 3, "Export this asset as an FBX")

            if exportSet is not None:
                if ui_assetLabelStyle is 1:
                    pass
                elif ui_assetLabelStyle is 2:
                    ui_setList.setItemDisplayLabel(item, exportSet.ExportFilename.get())
                elif ui_assetLabelStyle is 3:
                    ui_setList.setItemDisplayLabel(item, handler.GetOutputFile())
                elif ui_assetLabelStyle is 4:
                    ui_setList.setItemDisplayLabel(item, "{0}/{1}".format(exportSet.ExportLocation.get(),
                                                                          exportSet.ExportFilename.get()))
    else:
        if ui_assetLabelStyle is 1:
            pass
        else:
            newName = item.replace(parent + "|", "")
            ui_setList.setItemDisplayLabel(item, newName)
        


def uiSetChangeDetected(*args, **kwargs):
    if verbose: print("uiSetChangeDetected")
    eventManager.addIdleEventCallback(idleEventID, _refreshSetList)



def nodeDeletedCallback(*args, **kwargs):
    if verbose: print("nodeDeleted")
    global ui_setList
    
    depNode = events.getDepNode(args[0])
    nodeName = depNode.name()
    typeName = depNode.typeName()
    
    node = pm.ls(nodeName)[0]

    if typeName == u'objectSet':
        if verbose: print("ObjectSet Delete Detected")
        if ui_setList.itemExists(nodeName):
            ui_setList.removeItem(nodeName)
    else:
        for e in exportSets:
            if e.exists() is True:        
                print ("Node is {0}, type is {2}, set is {1}".format(node, e, typeName))
        
                thisItem = e.nodeName() + "|" + node.nodeName()
                itemPresent = ui_setList.itemExists(thisItem)
        
                if (itemPresent) is True:
                    ui_setList.removeItem(thisItem)
            else:
                if ui_setList.itemExists(e.nodeName()):
                    ui_setList.removeItem(e.nodeName())
                


def uiDeleteCallback(*args):
    """
    This is the function that will be called whenever the ui, passed to the MUiMessage.addUiDeletedCallback( window, uiDeleteCallback )
    is deleted
    """
    eventManager.removeCallback(uiSetAddedCallbackID)
    eventManager.removeCallback(uiSetRemovedCallbackID)
    eventManager.removeCallback(uiSetChangedCallbackID)
    eventManager.removeCallback(idleEventID)
    eventManager.removeCallback(uiDeletedCallbackID)

    eventManager.deregisterUserEvent(userEvent_setsChanged)
    eventManager.clearNameChangedCallbacks()


def _getSetForItem(item):
    if item in exportSets:
        return exportSets[exportSets.index(item)]


def _getSetForSelectedItem(*args):
    # TODO: assumed one selection @ahogan
    # TODO: assumed there is at least one item and at least one item is actually selected @ahogan
    global ui_setList
    selectedItems = ui_setList.getSelectedItems()

    if selectedItems is not None:
        if len(selectedItems) > 0:
            return _getSetForItem(selectedItems[0])
    else:
        pm.confirmDialog(title="Set Error", message="Please select an Asset before you perform that operation.")

        return None


def _getSelectedSets(*args):
    global ui_setList
    selectedItems = ui_setList.getSelectedItems()

    selectedSets = [_getSetForItem(item) for item in selectedItems]

    return selectedSets


def _refreshSetList(*args):
    if verbose: print("Refreshing...")
    global exportSets
    global ui_setList

    eventManager.removeCallback(idleEventID)
    eventManager.clearNameChangedCallbacks()

    # TODO:  !! So important - rework this so we are updating the list in place, not rebuilding it each refresh
    ui_setList.removeAll()

    exportSets = Assets.GetAssets()
    
    for exportSet in exportSets:       
        AddSetToSetList(exportSet)

    if verbose: print("...Done Refreshing")


def _onNodeRenamed(*args):  
    """ A callback function to rename list items """
    global ui_setList
    global exportSets
    
    oldName = args[1]

    depNode = events.getDepNode(args[0])
    newName = depNode.name()
    typeName = depNode.typeName()
        
    if typeName == u'objectSet':      
        if verbose: print("ObjectSet Rename Detected")
       
        items = ui_setList.getChildren()
        
        if items is not None and oldName in items:
            if verbose: print("Old ObjectSet Name found in list")
            index = ui_setList.getItemIndex(oldName)
            ui_setList.removeItem(oldName)

            objectSet = pm.ls(newName)[0]
            AddSetToSetList(objectSet, index=index)             
    else:
        if verbose: print("Node Rename Detected")
        
        node = pm.ls(newName)[0]
        
        for e in exportSets:
            if node in e:
                old_combinedName = e.nodeName() + "|" + oldName
                
                if ui_setList.itemExists(old_combinedName):
                    if verbose: print('Found {0} in setlist, attempting to replace with new name')
                    index = ui_setList.getItemIndex(old_combinedName)
                    ui_setList.removeItem(old_combinedName)
                    AddSetMemberToSetList(node, e.nodeName(), index=index)

def refreshMayaOutliner():
    editors = pm.lsUI(editors=True)
    for e in editors:
        if (pm.outlinerEditor(e, exists=True)):
            pm.outlinerEditor(e, edit=True, refresh=True)
            
                         
def toggleAssetOutlinerVisibility(*args):
    selectedItems = ui_setList.getSelectedItems()
    for item in selectedItems:
        if ui_setList.isLeaf(item):
            pass
        else:
            exportSet = pm.ls(item)[0]
            hidden = exportSet.hiddenInOutliner.get()
            exportSet.hiddenInOutliner.set(not hidden)

    
def copyFBXtoClipBoard(*args):
    paths = ""
    
    selectedItems = ui_setList.getSelectedItems()
    for item in selectedItems:
        if ui_setList.isLeaf(item):
            pass
        else:
            exportSet = pm.ls(item)[0]
            handler = Assets.GetHandlerForSet(exportSet)
            file = handler.GetOutputFile()
            file = os.path.normpath(file)
            
            paths = paths + file + "\n"

    pyperclip.copy(paths)
    
def copyFoldertoClipBoard(*args):
    paths = ""

    selectedItems = ui_setList.getSelectedItems()
    for item in selectedItems:
        if ui_setList.isLeaf(item):
            pass
        else:
            exportSet = pm.ls(item)[0]
            handler = Assets.GetHandlerForSet(exportSet)
            file = handler.GetOutputFolder()
            file = os.path.normpath(file)

            paths = paths + file + "\n"

    pyperclip.copy(paths)


def exploreToFBX(*args):
    selectedItems = ui_setList.getSelectedItems()
    for item in selectedItems:
        if ui_setList.isLeaf(item):
            pass
        else:
            exportSet = pm.ls(item)[0]
            handler = Assets.GetHandlerForSet(exportSet)
            folder = handler.GetOutputFolder()
            folder = os.path.normpath(folder)
            
            subprocess.Popen('explorer "{0}"'.format(folder))

def _createNewSet(*args):
    newSetName = "MyNewSet"
    sel = pm.selected()

    if len(sel) > 0:
        selObject = pm.selected()[0]

        if selObject is not None:
            newSetName = selObject.nodeName()

    pm.select(sel)
    newSet = Assets.Create(newSetName)

    pm.select(sel)
    
    exportSets.append(newSet)
    AddSetToSetList(newSet)
    

def _createNewSetForEach(*args):
    selectedItems = pm.selected()

    for sel in selectedItems:
        pm.select(sel)
        newSetName = sel.nodeName()
        newSet = Assets.Create(newSetName)
        exportSets.append(newSet)
        AddSetToSetList(newSet)

    pm.select(selectedItems)
    

def _addSelectionToSet(*args):
    if verbose: print 'addSelectionToSet str=' + args[0] + ' onoff= ' + str(args[1])
    item = args[0]  #item is the name of the set -- ie pCube1_EXPORT
    
    theSet = _getSetForItem(item)
    selection = pm.selected()
        
    if theSet is not None:
        theSet.addMembers(selection)
    
    global ui_setList
    global exportSets
    
    #now make sure the (possibly) new children show up in the Dex ui
    for s in selection:
        AddSetMemberToSetList(s, item)          
        


def _removeSelectionFromSet(*args):
    if verbose: print 'add str= ' + args[0] + ' onoff= ' + str(args[1])
    theSet = _getSetForItem(args[0])
    
    selection = pm.selected()
    
    if theSet is not None:
        for s in selection:
            if s in theSet:
                theSet.removeMembers([s])
            
            RemoveSetMemberFromList(s, theSet)


def AddSetToSetList(objectSet, index=None):
    if verbose: print("AddSetToSetList: Adding {0}".format(objectSet.nodeName()))
    item = objectSet.name()

    if (index is None):
        ui_setList.addItem(item)
    else:
        ui_setList.insertItem(item, "", index)

    eventManager.registerNameChangedCallback(objectSet.name() + "_onRename", _onNodeRenamed, node=objectSet)

    for m in objectSet.members():
        AddSetMemberToSetList(m, item)
        
def AddSetMemberToSetList(pnSetMember, parentItem, index=None):
    if verbose: print("AddSetMemberToSetList:".format(pnSetMember.nodeName(), parentItem))
    global ui_setList

    childName = parentItem + "|" + pnSetMember.nodeName()
    
    if ui_setList.itemExists(childName) is False:
        if verbose: print("\tAdding {0} to {1}".format(pnSetMember.nodeName(), parentItem))
        
        if index is None:
            ui_setList.addItem(childName, parentItem, bHideButtons=True)
        else:
            ui_setList.insertItem(childName, parentItem, index, bHideButtons=True)

        eventManager.registerNameChangedCallback(childName + "_onRename", _onNodeRenamed, node=pnSetMember)


def RemoveSetMemberFromList(pnSetMember, parentItem):
    if verbose: print("RemoveSetMemberFromList:".format(pnSetMember.nodeName(), parentItem))
    global ui_setList

    childName = parentItem + "|" + pnSetMember.nodeName()
    

    if ui_setList.itemExists(childName) is True:
        if verbose: print("\tRemoving {0} from {1}".format(pnSetMember.nodeName(), parentItem))
        ui_setList.removeItem(childName)
        
def _editExportSet(*args):
    theSet = _getSetForSelectedItem()
    if theSet is not None:
        reload(esd)  # TODO optimize this a bit
        esd.editSetDialog(theSet)


def _deleteExportSet(*args):
    theSet = _getSetForSelectedItem()
    if theSet is not None:
        pm.delete(theSet)

    _refreshSetList()


def _deleteSelectedExportSets(*args):
    theSets = _getSelectedSets()

    pm.delete(theSets)

    _refreshSetList()


def _exportSelectedSets(*args):
    if verbose: print 'exp str= ' + args[0] + ' onoff= ' + str(args[1])
    scene = pm.sceneName()  # Result: Path('D:/Dante/geo/bell_b.ma') #     
    if scene == "":
        msg = "Dex works with relative paths, so you will have to save the scene before you can export.  Sorry for the inconvenience!"
        pm.confirmDialog(title="Please save the Scene", message=msg)
    else:
        theSet = _getSetForItem(args[0])
        if theSet is not None:
            Assets.Export(theSet)


def _exportAllSets(*args):
    scene = pm.sceneName()  # Result: Path('D:/Dante/geo/bell_b.ma') #     
    if scene == "":
        msg = "Dex works with relative paths, so you will have to save the scene before you can export.  Sorry for the inconvenience!"
        pm.confirmDialog(title="Please save the Scene", message=msg)
    else:
        for theSet in exportSets:
            if theSet is not None:
                Assets.Export(theSet)


def _onListSelectCommand(*args):
    if verbose:print 'selection str= ' + args[0] + ' onoff= ' + str(args[1])
    # theSet = _getSetForItem(args[0])
    # if theSet is not None:
    # pm.select(theSet, noExpand=True)

    return True


def _onUserEditLabel(item, newDisplayName):
    """The callback function to be invoked when the user changes the name of an 
            item by double clicking it in the UI. 
        Accepts two string arguments: the item name and the new name. 
        The item name refers to the name of the item and not the display label. 
        The callback function should return a string. 
        - An empty string indicates that the rename operation was invalid and the control 
            should revert to the original name. 
        - If the rename operation is valid the callback should return a string that identifies 
            the item, possibly different from the new display name entered by the user."""

    if verbose: print("_onUserEditLabel   Item: {0}    NewDisplayName: {1}".format(item, newDisplayName))
    global ui_setList
    global ui_assetLabelStyle

    asset = Assets.GetAsset(item)
    exportSet = Assets.GetAsset(item)
    handler = Assets.GetHandlerForSet(exportSet)

    if exportSet is not None:
        if ui_assetLabelStyle is 1:
            exportSet.rename(newDisplayName)
        elif ui_assetLabelStyle is 2:
            asset.ExportFilename.set(newDisplayName)
        elif ui_assetLabelStyle is 3:
            ui_setList.setItemDisplayLabel(item, handler.GetOutputFile())

    return item


def _onListDoubleClick(*args):
    theSet = _getSetForSelectedItem()
    if theSet is not None:
        pm.select(theSet.members(), noExpand=True)
