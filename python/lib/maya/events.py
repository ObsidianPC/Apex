import maya.OpenMaya as om
import maya.OpenMayaUI as omui

verbose=False

class eventManager(dict):
    def __init__(self):
        self.events = dict()
        self.userEvents = dict()
        self.nameChangedEvents = dict()

    def addUiDeletedCallback(self, uiElement, strCallbackName, fnCallback):
        callbackID = omui.MUiMessage.addUiDeletedCallback(uiElement, fnCallback)
        self.events[strCallbackName] = callbackID
        return callbackID

    def addNodeAddedCallback(self, strCallbackName, fnCallback, **kwargs):
        callbackID = None
        if "strNodeType" in kwargs:
            callbackID = om.MDGMessage.addNodeAddedCallback(fnCallback, kwargs["strNodeType"])
        else:
            callbackID = om.MDGMessage.addNodeAddedCallback(fnCallback)
        
        self.events[strCallbackName] = callbackID
        return callbackID

    def addNodeRemovedCallback(self, strCallbackName, fnCallback, **kwargs):
        callbackID = None
        
        if "strNodeType" in kwargs:
            callbackID = om.MDGMessage.addNodeRemovedCallback(fnCallback, kwargs["strNodeType"])
        else:
            callbackID = om.MDGMessage.addNodeRemovedCallback(fnCallback)
            
        self.events[strCallbackName] = callbackID
        return callbackID

    def addIdleEventCallback(self, strCallbackName, fnCallback):
        if strCallbackName not in self.events:
            callbackID = om.MEventMessage.addEventCallback("idle", fnCallback)
            self.events[strCallbackName] = callbackID
            return callbackID
        else:
            return self.events[strCallbackName]

    def registerUserEvent(self, strCallbackName, fnCallback):
        if not om.MUserEventMessage.isUserEvent(strCallbackName):
            om.MUserEventMessage.registerUserEvent(strCallbackName)
            self.userEvents[strCallbackName] = strCallbackName

        callbackID = om.MUserEventMessage.addUserEventCallback(strCallbackName, fnCallback)
        self.userEvents[strCallbackName] = callbackID

        return callbackID

    def deregisterUserEvent(self, strCallbackName):
        if om.MUserEventMessage.isUserEvent(strCallbackName):
            om.MUserEventMessage.deregisterUserEvent(strCallbackName)

        if self.userEvents.has_key(strCallbackName):
            self.userEvents.pop(strCallbackName)

    def removeCallback(self, strCallbackName):
        """ Remove a specific callback by it's event name"""

        if self.events.has_key(strCallbackName) and self.events[strCallbackName] is not None:
            om.MMessage.removeCallback(self.events[strCallbackName])
            del self.events[strCallbackName]
            self.events.pop(strCallbackName, None)
            return True
        else:
            return False

    def registerNameChangedCallback(self, strCallbackName, func, node=None):
        """ Registers a NameChanged callback for the specified node

        Args:
        node: PyNode you want to listen to for renaming events
        func: a callable to call when the event is triggered.

        Return:
        callback_id: Pass this to removeCallback to cleanup the trigger
        """

        # Note:
        # passing in a null MObject (ie, without a name as an argument)
        # registers the callback to get all name changes in the scene
        # if you wanted to monitor a specific object's name changes
        # you could pass a name to the MObject
        
        if verbose: print("Registering {0} with fn {1}".format(node, func))

        mObj = None
        if node is not None:
            mObj = node.__apimobject__()
        else:
            mObj = om.MObject()    
        
        
        callbackID = om.MNodeMessage.addNameChangedCallback(mObj, func)
        self.nameChangedEvents[strCallbackName] = callbackID
        return callbackID

    def removeNameChangedCallback(self, strCallbackName):
        """ Remove a specific callback by it's event name"""

        if self.nameChangedEvents.has_key(strCallbackName) and self.nameChangedEvents[strCallbackName] is not None:
            om.MMessage.removeCallback(self.nameChangedEvents[strCallbackName])
            del self.nameChangedEvents[strCallbackName]
            self.nameChangedEvents.pop(strCallbackName, None)
            return True
        else:
            return False
    
    def clearNameChangedCallbacks(self):
        keys = self.nameChangedEvents.keys()
        
        for k in keys:
            self.removeNameChangedCallback(k)

def getDepNode(obj):
    return om.MFnDependencyNode(obj)


def __exampleNameChangedCallback( *args):
    """ An example callback function to demonstrate hooking object renames """
    # convert the MObject to a dep node
    depNode = getDepNode(args[0])
    oldName = args[1]

    print('----\nNameChangedCallback')
    print('newName: ', depNode.name())
    print('oldName', oldName)
    print('type', depNode.typeName())


maya2018eventNames = [u'ActiveViewChanged',
 u'ChannelBoxLabelSelected',
 u'ColorIndexChanged',
 u'CurveRGBColorChanged',
 u'DagObjectCreated',
 u'DisplayColorChanged',
 u'DisplayPreferenceChanged',
 u'DisplayRGBColorChanged',
 u'DragRelease',
 u'EditModeChanged',
 u'LiveListChanged',
 u'MenuModeChanged',
 u'ModelPanelSetFocus',
 u'NameChanged',
 u'NewSceneOpened',
 u'PolyUVSetChanged',
 u'PolyUVSetDeleted',
 u'PostSceneRead',
 u'PostSceneSegmentChanged',
 u'PostToolChanged',
 u'PreFileNew',
 u'PreFileNewOrOpened',
 u'PreFileOpened',
 u'PreSelectionChangedTriggered',
 u'RebuildUIValues',
 u'RecentCommandChanged',
 u'Redo',
 u'RenderSetupSelectionChanged',
 u'RenderViewCameraChanged',
 u'SceneImported',
 u'SceneOpened',
 u'SceneSaved',
 u'SceneSegmentChanged',
 u'SelectModeChanged',
 u'SelectPreferenceChanged',
 u'SelectPriorityChanged',
 u'SelectTypeChanged',
 u'SelectionChanged',
 u'SequencerActiveShotChanged',
 u'SetModified',
 u'ToolChanged',
 u'ToolDirtyChanged',
 u'ToolSettingsChanged',
 u'Undo',
 u'UvTileProxyDirtyChangeTrigger',
 u'activeHandleChanged',
 u'angularToleranceChanged',
 u'angularUnitChanged',
 u'animLayerAnimationChanged',
 u'animLayerBaseLockChanged',
 u'animLayerGhostChanged',
 u'animLayerLockChanged',
 u'animLayerRebuild',
 u'animLayerRefresh',
 u'axisAtOriginChanged',
 u'cameraChange',
 u'cameraDisplayAttributesChange',
 u'colorMgtConfigChanged',
 u'colorMgtConfigFileEnableChanged',
 u'colorMgtConfigFilePathChanged',
 u'colorMgtEnabledChanged',
 u'colorMgtOCIORulesEnabledChanged',
 u'colorMgtOutputChanged',
 u'colorMgtPlayblastOutputChanged',
 u'colorMgtPrefsReloaded',
 u'colorMgtPrefsViewTransformChanged',
 u'colorMgtRefreshed',
 u'colorMgtUserPrefsChanged',
 u'colorMgtWorkingSpaceChanged',
 u'constructionHistoryChanged',
 u'cteEventClipEditModeChanged',
 u'cteEventKeyingTargetForClipChanged',
 u'cteEventKeyingTargetForInvalidChanged',
 u'cteEventKeyingTargetForLayerChanged',
 u'currentContainerChange',
 u'currentSoundNodeChanged',
 u'customEvaluatorChanged',
 u'dbTraceChanged',
 u'deleteAll',
 u'displayLayerAdded',
 u'displayLayerChange',
 u'displayLayerDeleted',
 u'displayLayerManagerChange',
 u'displayLayerVisibilityChanged',
 u'freezeOptionsChanged',
 u'glFrameTrigger',
 u'graphEditorChanged',
 u'graphEditorOutlinerHighlightChanged',
 u'graphEditorOutlinerListChanged',
 u'graphEditorParamCurveSelected',
 u'gridDisplayChanged',
 u'idle',
 u'idleHigh',
 u'idleVeryLow',
 u'interactionStyleChanged',
 u'lightLinkingChanged',
 u'lightLinkingChangedNonSG',
 u'linearToleranceChanged',
 u'linearUnitChanged',
 u'metadataVisualStatusChanged',
 u'modelEditorChanged',
 u'nurbsCurveRebuildPrefsChanged',
 u'nurbsToPolygonsPrefsChanged',
 u'nurbsToSubdivPrefsChanged',
 u'passContributionMapChange',
 u'playbackModeChanged',
 u'playbackRangeChanged',
 u'playbackRangeSliderChanged',
 u'playbackSpeedChanged',
 u'polyCutUVEventTexEditorCheckerDisplayChanged',
 u'polyCutUVShowTextureBordersChanged',
 u'polyCutUVShowUVShellColoringChanged',
 u'polyCutUVSteadyStrokeChanged',
 u'polyTopoSymmetryValidChanged',
 u'poseEditorTreeviewSelectionChanged',
 u'preferredRendererChanged',
 u'quitApplication',
 u'redoXformCmd',
 u'renderLayerChange',
 u'renderLayerManagerChange',
 u'renderPassChange',
 u'renderPassSetChange',
 u'renderPassSetMembershipChange',
 u'sculptMeshCacheBlendShapeListChanged',
 u'sculptMeshCacheCloneSourceChanged',
 u'selectionConstraintsChanged',
 u'selectionPipelineChanged',
 u'serialExecutorFallback',
 u'shapeEditorTreeviewSelectionChanged',
 u'snapModeChanged',
 u'softSelectOptionsChanged',
 u'start3dPaintTool',
 u'startColorPerVertexTool',
 u'stop3dPaintTool',
 u'stopColorPerVertexTool',
 u'symmetricModellingOptionsChanged',
 u'tabletModeChanged',
 u'teClipAdded',
 u'teClipModified',
 u'teClipRemoved',
 u'teCompositionActiveChanged',
 u'teCompositionAdded',
 u'teCompositionNameChanged',
 u'teCompositionRemoved',
 u'teEditorPrefsChanged',
 u'teMuteChanged',
 u'texMoveContextOptionsChanged',
 u'texRotateContextOptionsChanged',
 u'texScaleContextOptionsChanged',
 u'texWindowEditorCheckerDensityChanged',
 u'texWindowEditorCheckerDisplayChanged',
 u'texWindowEditorClose',
 u'texWindowEditorDisplaySolidMapChanged',
 u'texWindowEditorImageBaseColorChanged',
 u'texWindowEditorShowup',
 u'threadCountChanged',
 u'timeChanged',
 u'timeUnitChanged',
 u'transformLockChange',
 u'undoSupressed',
 u'undoXformCmd',
 u'workspaceChanged',
 u'xformConstraintOptionsChanged'] 