import maya.OpenMaya as om
import maya.OpenMayaUI as omui

import lib.maya.ui as lmui
import lib.maya.events as lmevents
reload(lmevents)

import pymel.core as pm

eventPrefix = "uiTest"

class ui(lmui.ui):

    uiSetAddedCallbackID = eventPrefix + "_uiSetAddedCallbackID"
    uiSetRemovedCallbackID = eventPrefix + "_uiSetRemovedCallbackID"
    uiSetChangedCallbackID = eventPrefix + "_uiSetChangedCallbackID"
    testUIClosedCallbackID = eventPrefix + "_uiClosedCallbackID"
    testUI_idleEvent = eventPrefix + "_idleCallbackID"

    def __init__(self):
        super(ui, self).__init__()
        print "child ui __init__"

        ui.instance = self

        self.windowName = "uiTest"
        self.windowTitle = "Test Window - Set Lister"

        self.events.addNodeAddedCallback(ui.uiSetAddedCallbackID, "objectSet", self.uiSetChangeDetected)
        self.events.addNodeRemovedCallback(ui.uiSetRemovedCallbackID, "objectSet", self.uiSetChangeDetected)
        self.events.registerUserEvent(ui.uiSetChangedCallbackID, self.refreshSetList)


    def createTopLayout(self, *args):
        button = pm.button(label="A Test Button", command=self.testButtonClick)
        return button

    def createMiddleLayout(self, *args):
        self.setList = pm.textScrollList(selectCommand=self.onListSelectCommand, doubleClickCommand=self.onListDoubleClick)
        return self.setList

    def createBottomLayout(self, *args):
        with pm.rowLayout(numberOfColumns=5,
                                  adjustableColumn=3,                                
                                  columnWidth5=[50,50,50,50,50],
                                  columnAttach5=["both", "both", "both", "both", "both"],
                                  columnAlign5=["center","center","center","center","center"]) as buttonBar:

            pm.button(label="A", height=50, command=self.testButtonClick, annotation="Hmmm...")
            pm.button(label="B", height=50, command=self.testButtonClick, annotation="Hmmm...")
            pm.button(label="C", height=50, command=self.testButtonClick, annotation="Hmmm...")
            pm.button(label="D", height=50, command=self.testButtonClick, annotation="Hmmm...")
            pm.button(label="E", height=50, command=self.testButtonClick, annotation="Hmmm...")

        return buttonBar

    def createUI(self):
        print("TestUI CreateUI Start")
        super(ui, self).createUI()

        self.uiSetChangeDetected()

        print("TestUI CreateUI Done")

    def uiDeleteCallback(self, *args):
        """
        Override this in your derived class and it will be called.  Remember to call it's super!
        """
        super(ui, self).uiDeleteCallback(*args)

        print "TestUI DeleteUI Callback"

        self.events.removeCallback(ui.uiSetAddedCallbackID)
        self.events.removeCallback(ui.uiSetRemovedCallbackID)

        self.events.deregisterUserEvent(ui.uiSetChangedCallbackID)
        self.events.removeCallback(ui.uiSetChangedCallbackID)

        self.events.removeCallback(ui.testUI_idleEvent)
        self.events.removeCallback(ui.uiClosedCallbackID)

        print "TestUI DeleteUI Finished!"

    def uiSetChangeDetected(self, *args):
        print "SetChangeDetected"
        self.events.addIdleEventCallback(ui.testUI_idleEvent, self.refreshSetList)

    def refreshSetList(self, *args):
        print("TestUI Refreshing set list")

        self.events.removeCallback(ui.testUI_idleEvent)

        for k, v in self.events.nameChangedEvents.items():
            self.events.removeNameChangedCallback(v)

        self.events.nameChangedEvents.clear()

        self.setList.removeAll()

        exportSets = pm.ls(type='objectSet')

        for mySet in exportSets:
            self.setList.append(mySet.name())
            self.events.registerNameChangedCallback(eventPrefix + mySet.name(), mySet, self.onSetRenamed)

    def onSetRenamed(self, *args):
        """ A callback function to rename list items """
        node = args[0]
        # convert the MObject to a dep node
        depNode = om.MFnDependencyNode(node)
        oldName = args[1]
        newName = depNode.name()
        typeName = depNode.typeName()

        items = self.setList.getAllItems()

        if oldName in items:
            index = items.index(oldName)
            self.setList.removeIndexedItem(index + 1)
            self.setList.appendPosition([index + 1, newName])

    def onListSelectCommand(self, *args):
        print("List Select")

    def onListDoubleClick(self, *args):
        print("List DoubleClick")

    def testButtonClick(self, *args):
        print("TestUI Test Button Clicked")