verbose = True
if verbose:print("> animationAsset loading")

import baseAsset

import Assets 

import pymel.core as pm


class animationAsset(baseAsset.baseAsset):
    stringId = "animation"
    
    def __init__(self, exportSet):
        super(animationAsset, self).__init__(exportSet)
        if verbose:print "animationAsset constructor"
        self.stringId = "animation"

    def InitializeSet(self):
        super(animationAsset, self).InitializeSet()
        if verbose: print "animationAsset InitializeSet"

        if not self.set.hasAttr("StartFrame"):
            self.set.addAttr("StartFrame", at="short")

        if not self.set.hasAttr("EndFrame"):
            self.set.addAttr("EndFrame", at="short")

    def SetFBXOptions(self):
        super(animationAsset, self).SetFBXOptions()
        if verbose: print "Setting animationAsset FBX Settings"


        self.settings['Export|IncludeGrp|Animation']['VALUE'] = "true"

        self.settings['Export|IncludeGrp|Animation|ExtraGrp|Quaternion']['VALUE'] = "Retain Quaternion Interpolation"

        
        # Allows for baking of constrained channels or more exotic simulations
        self.settings['Export|IncludeGrp|Animation|BakeComplexAnimation']['VALUE'] = "true"
        self.settings['Export|IncludeGrp|Animation|BakeComplexAnimation|BakeFrameStart']['VALUE'] = self.set.StartFrame.get()
        self.settings['Export|IncludeGrp|Animation|BakeComplexAnimation|BakeFrameEnd']['VALUE'] = self.set.EndFrame.get()
        self.settings['Export|IncludeGrp|Animation|BakeComplexAnimation|BakeFrameStep']['VALUE'] = "1"
        self.settings['Export|IncludeGrp|Animation|BakeComplexAnimation|ResampleAnimationCurves']['VALUE'] = "true"

        # root joint not exported if this is true
        # settings['Export|IncludeGrp|Geometry|AnimationOnly']['VALUE'] = "true"

        # root joint not exported if this is false
        self.settings['Export|IncludeGrp|InputConnectionsGrp|InputConnections']['VALUE'] = "true"

        # if this is set to true, no joint-constrained animation is brought in
        # settings['Export|IncludeGrp|Animation|ConstraintsGrp|Constraint']['VALUE'] = "true"

    def PreExport(self):
        super(animationAsset, self).PreExport()

        self.data["OriginalStartFrame"] = pm.playbackOptions(query=True, minTime=True)
        self.data["OriginalEndFrame"] = pm.playbackOptions(query=True, maxTime=True)

        pm.playbackOptions(minTime=self.set.StartFrame.get())
        pm.playbackOptions(maxTime=self.set.EndFrame.get())

        pm.autoKeyframe(state=False)

    def PostExport(self):
        super(animationAsset, self).PostExport()

        pm.playbackOptions(minTime=self.data["OriginalStartFrame"])
        pm.playbackOptions(maxTime=self.data["OriginalEndFrame"])

    def DrawCustomUI(self, parentControl):
        super(animationAsset, self).DrawCustomUI(parentControl)
        if verbose: print("--> animation asset DrawCustomUI")

        widget = animationAssetWidget.create(parentControl, self.set)

        return widget


class animationAssetWidget(pm.uitypes.ColumnLayout):

    def connectFrameControls(self):
        pm.connectControl(self.StartFrame, self.set.StartFrame)
        pm.connectControl(self.EndFrame, self.set.EndFrame)

    def Initialize(self, theSet):
        self.owner = None
        self.set = theSet
        self.assetHandler = Assets.GetHandlerForSet(self.set)
        
        pm.rowLayout(nc=9)
        
        pm.text(label="                      ")

        pm.text(label="Start Frame: ")
        self.StartFrame = pm.intField(width=50)

        pm.text(label=" ")

        pm.text(label="End Frame: ")
        self.EndFrame = pm.intField(width=50)

        self.connectFrameControls()

        
        pm.setParent(self)


        pm.rowLayout(nc=5)

        pm.text(label="                      ")
        pm.button(label="Take From Scene", command=self.TakeSceneTimeRange)

        pm.text(label="  ")

        pm.text(label="  ")
        pm.button(label="Match scene to Anim", command=self.MapSceneToMotionTimeRage)

    def TakeSceneTimeRange(self, *args):
        self.set.StartFrame.set(int(pm.playbackOptions(query=True, minTime=True)))
        self.set.EndFrame.set(int(pm.playbackOptions(query=True, maxTime=True)))

    def MapSceneToMotionTimeRage(self, *args):
        pm.playbackOptions(minTime=self.set.StartFrame.get())
        pm.playbackOptions(maxTime=self.set.EndFrame.get())
        pm.currentTime(self.set.StartFrame.get())

        pm.timeControl(pm.melGlobals['gPlayBackSlider'], edit=True, forceRefresh=True)

        #pm.refresh(force=True)

    @staticmethod
    def create(parent, theSet, *args):
        pm.setParent(parent)
        s = animationAssetWidget(adjustableColumn=True)
        s.Initialize(theSet)

        return s