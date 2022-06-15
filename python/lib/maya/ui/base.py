import pymel.core as pm
import lib.maya.events as lmevents

class ui(object):
    """This class is a demo class for a ui window utility base class with built in events"""
    uiClosedCallbackID = "genericUI_uiClosedCallbackID"
    idleEventID = "genericUI_idleEventID"

    instance = None
    

    def createTopLayout(self, *args):
        button = pm.button(label="A Test Button", command=self.testButtonClick)
        return button

    def createMiddleLayout(self, *args):
        button = pm.button(label="A Test Button", command=self.testButtonClick)
        return button

    def createBottomLayout(self, *args):
        button = pm.button(label="A", height=50, command=self.testButtonClick, annotation="Hmmm...")
        return button


    @classmethod
    def soundOff(cls, *args):
        print("Sounding off: " + str(cls))

    def __init__(self):
        print("Base UI __init__")
        ui.soundOff(self.__class__)
        ui.instance = self

        self.windowName = "GenericWindow"
        self.windowTitle = "Generic Window with Header and Footer"
        
        self.window = None

        self.uiWidth=250
        self.uiHeight=650

        self.uiBuffer=5
        self.events = lmevents.eventManager()


    def createUI(self):
        print "base CreateUI Start"

        # Delete other instances of this tool window
        if pm.window(self.windowName, exists=True):
            pm.deleteUI(self.windowName)

        # Reset Window Preferences
        #TODO Tie to a ui toggle somewhere
        if pm.windowPref(self.windowName, exists=True):
            pm.windowPref(self.windowName, remove=True)

        with pm.window(self.windowName, title=self.windowTitle, width=self.uiWidth, height=self.uiHeight, sizeable=True) as self.window:

            with pm.formLayout(numberOfDivisions=100) as self.form:

                TopLayout = self.createTopLayout()

                MiddleLayout = self.createMiddleLayout()
                
                BottomLayout = self.createBottomLayout()
                

            pm.formLayout( self.form,
                          edit=True,
                          attachForm=[(TopLayout, 'top', self.uiBuffer),
                                      (TopLayout, 'left', self.uiBuffer),
                                      (TopLayout, 'right', self.uiBuffer),
                                      (MiddleLayout, 'left', self.uiBuffer),
                                      (MiddleLayout, 'right', self.uiBuffer),
                                      (BottomLayout, 'left', self.uiBuffer),
                                      (BottomLayout, 'right', self.uiBuffer),
                                      (BottomLayout, 'bottom', self.uiBuffer)
                                      ],
                          attachControl=[(MiddleLayout, 'top', self.uiBuffer, TopLayout),
                                         (MiddleLayout, 'bottom', self.uiBuffer, BottomLayout)],
                          attachNone=(BottomLayout, 'top')                                        
                          )

        self.window.show()

        #set up callbacks
        print("Registering uiDeleteCallback in baseCreateUI: " + str(self.uiDeleteCallback))

        self.events.addUiDeletedCallback(self.window, ui.uiClosedCallbackID, self.uiDeleteCallback)
        print("base CreateUI End")

        return self


    def uiDeleteCallback(self, *args):
        """
        Override this in your derived class and it will be called.  Remember to call it's super!
        """
        print "BaseUI DeleteUI Callback"
        self.events.removeCallback(ui.uiClosedCallbackID)
        print "base DeleteUI Finished!"

    def testButtonClick(self, *args):
        print("test button clicked")
    
