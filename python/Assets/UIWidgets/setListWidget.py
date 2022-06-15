import pymel.core as pm


def selectTreeCallBack(*args):
    # print 'selection :- str= ' + args[0] + ' onoff= ' + str(args[1])
    return True


def pressTreeCallBack(*args):
    # print 'press :- str= ' + args[0] + ' onoff= ' + str(args[1])
    return True


class setList(object):
    control = None

    def __init__(self, *args):
        self.control = pm.treeView(numberOfButtons=3, abr=False)
        self.setAllowReparenting(False)
        # self.setPressCommand([(1, pressTreeCallBack), (2, pressTreeCallBack), (3, pressTreeCallBack)])
        # self.setSelectCommand(selectTreeCallBack)

    def enableLabel(self, sItem, iOnOff):
        pm.treeView(self.control, e=True, enableLabel=[sItem, iOnOff])

    def setAllowMultiSelection(self, allowMultiSelect):
        pm.treeView(self.control, e=True, allowMiltiSelection=allowMultiSelect)

    def setAllowReparenting(self, allReparent):
        pm.treeView(self.control, e=True, allowReparenting=allReparent)

    def setAttachButtonRight(self, attachRight):
        """0 = left, 1 = right"""
        pm.treeView(self.control, e=True, attachButtonRight=attachRight)

    def setButtonState(self, item, button, buttonState):
        pm.treeView(self.control, e=True, buttonState=[item, button, buttonState])

    def setButtonStyle(self, item, button, buttonStyle):
        """ButtonStyle can be pushButton, 2StateButton, 3StateButton"""
        pm.treeView(self.control, e=True, buttonStyle=[item, button, buttonStyle])

    def setButtonTextIcon(self, item, button, text):
        pm.treeView(self.control, e=True, buttonTextIcon=[item, button, text])

    def setButtonTooltip(self, item, button, tooltip):
        pm.treeView(self.control, e=True, buttonTooltip=[item, button, tooltip])

    def addItem(self, item, parent="", bHideButtons=False):
        # print("setList adding " + item + " with parent " + parent)
        pm.treeView(self.control, e=True, addItem=[item, parent], expandItem=[item, False], hideButtons=bHideButtons)

    def clearSelection(self):
        pm.treeView(self.control, e=True, clearSelection=True)

    def getChildren(self):
        return pm.treeView(self.control, q=True, children=None)

    def isItemSelected(self, item):
        return pm.treeView(self.control, q=True, itemSelected=item)

    def insertItem(self, item, parent, index, bHideButtons=False):
        # print("Inserting Item")
        pm.treeView(self.control, e=True, insertItem=[item, parent, index], hideButtons=bHideButtons)
        
    def itemExists(self, item):
        iResult = pm.treeView(self.control, q=True, itemExists=item)
        
        if iResult is 1: 
            return True
        
        return False

    def getSelectedItems(self):
        return pm.treeView(self.control, q=True, selectItem=True)

    def setItemSelected(self, item, selectedState):
        pm.treeView(self.control, e=True, selectItem=[item, selectedState])

    def setItemDisplayLabel(self, item, label):
        pm.treeView(self.control, e=True, displayLabel=[item, label])

    def setItemDisplayLabelSuffix(self, item, labelSuffix):
        pm.treeView(self.control, e=True, displayLabelSuffix=[item, labelSuffix])

    def setButtonImage(self, item, buttonNum, imageName):
        pm.treeView(self.control, e=True, image=[item, buttonNum, imageName])

    def removeItem(self, item):
        pm.treeView(self.control, e=True, removeItem=item)

    def ornament(self, ornamentArray):
        pm.treeView(self.control, e=True, ornament=ornamentArray)

    def setNumberOfButtons(self, buttonCount):
        pm.treeView(self.control, e=True, numberOfButtons=buttonCount)

    def removeAll(self):
        pm.treeView(self.control, e=True, removeAll=True)

    def getItemExists(self, item):
        return pm.treeView(self.control, q=True, itemExists=item)

    def getItemIndex(self, item):
        return pm.treeView(self.control, q=True, itemIndex=item)

    def isLeaf(self, item):
        return pm.treeView(self.control, q=True, isLeaf=item)

    def setPressCommand(self, pressCommandArray):
        pm.treeView(self.control, e=True, pressCommand=pressCommandArray)

    def setRightPressCommand(self, pressCommandArray):
        pm.treeView(self.control, e=True, rightPressCommand=pressCommandArray)

    def setRenameCommand(self, renameCommand):
        print("setListWidget running setRenameCommand")
        pm.treeView(self.control, e=True, itemRenamedCommand=renameCommand)
        """	Set the callback function to be invoked when an item in the tree has been renamed.
         This occurs if there is a successful return of the command attached by "editLabelCommand" 
         or unconditionally if there is no editLabelCommand. The callback should accept two strings, 
         the old name and the new name of the item that was renamed."""

    def setEditLabelCommand(self, userEditLabelCommand):
        print("setListWidget running setEditLabelCommand")
        pm.treeView(self.control, e=True, editLabelCommand=userEditLabelCommand)
        """	Set the callback function to be invoked when the user changes the name of an 
        item by double clicking it in the UI. The callback should accept two string 
        arguments: the item name and the new name. The item name refers to the name of 
        the item and not the display label. The callback function should return a string. 
        An empty string indicates that the rename operation was invalid and the control 
        should revert to the original name. If the rename operation is valid the callback 
        should return a string that identifies the item, possibly different from the new 
        display name entered by the user."""

    def setSelectCommand(self, selectCommand):
        pm.treeView(self.control, e=True, selectCommand=selectCommand)

    def setItemDoubleClickCommand(self, doubleClickCommand):
        pm.treeView(self.control, e=True, itemDblClickCommand=doubleClickCommand)

    def setItemDoubleClickCommand2(self, doubleClickCommand2):
        pm.treeView(self.control, e=True, itemDblClickCommand2=doubleClickCommand2)

    def setItemAnnotation(self, item, annotation):
        pm.treeView(self.control, e=True, itemAnnotation=[item, annotation])

    def getItemAnnotation(self, item):
        return pm.treeView(self.control, q=True, itemAnnotation=True, item=item)
    
    def itemParent(self, item):
        return pm.treeView(self.control, q=True, itemParent=item)


def createSetList():
    sl = setList()
    return sl
