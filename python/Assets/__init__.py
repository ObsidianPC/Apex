import pymel.core as pm
import os
import re

import Assets.AssetHandlers.baseAsset as baseAsset
reload(baseAsset)

import Assets.AssetHandlers.staticMeshAsset as staticMeshAsset
reload(staticMeshAsset)

import Assets.AssetHandlers.skinnedMeshAsset as skinnedMeshAsset
reload(skinnedMeshAsset)

import Assets.AssetHandlers.animationAsset as animationAsset
reload(animationAsset)

pm.loadPlugin("fbxmaya.mll", quiet=True)

assetTypes = {
    "default": baseAsset.baseAsset,
    "staticMesh": staticMeshAsset.staticMeshAsset,
    "skinnedMesh": skinnedMeshAsset.skinnedMeshAsset,
    "animation": animationAsset.animationAsset
}


class AssetTypes:
    default = baseAsset.baseAsset
    StaticMesh = staticMeshAsset.staticMeshAsset
    SkinnedMesh = skinnedMeshAsset.skinnedMeshAsset


def expandMacros(inString):
    # If you have project macros in your path, expand them here!
    # TODO: This is on hold till later..... @ahogan

    #results = re.sub(re.escape("$$"), ".", inString, flags=re.IGNORECASE)
    #results = re.sub(re.escape("$"), ".", results, flags=re.IGNORECASE)
    #results = re.sub(re.escape("{WORKSPACE}"), expansionFunctionWorkspace(), results, flags=re.IGNORECASE)
    #results = results.replace("//", "/")
    #results = re.sub(re.escape("$"), ".", inString, flags=re.IGNORECASE)      
    
    return inString


def toLocalPath(assetOutputPath):
    scene = pm.sceneName()  # Result: Path('D:/Dante/geo/bell_b.ma') #
    sceneDir = os.path.dirname(scene)  # Result: u'D:/Dante/geo' #

    if assetOutputPath[0] == ".":
        # TODO: if exportLocation is . and file is not saved??         
        assetOutputPath = (sceneDir + "/" + assetOutputPath)
        
    localPath = os.path.normpath(assetOutputPath)
    localPath = localPath.replace("\\", "/")

    absPath = expandMacros(localPath)

    return absPath


def GetHandlerForSet(theSet):
    #print("Getting an asset handler for the set")
    if theSet.hasAttr("AssetType"):
        assetType = theSet.AssetType.get()
        if assetType in assetTypes:
            return assetTypes[assetType](theSet)
        else:
            pm._logger.error("Error: AssetHandler not found for : " + assetType + " - defaulting to StaticMesh")
            return assetTypes["StaticMesh"]

    else:
        raise ("AssetHandler Unable to be Determined")


def GetSceneSettings():
    # use selected items if there is a selection
    settingsNodes = pm.ls("DEX_SCENE_SETTINGS")
    sceneSettings = None

    if len(settingsNodes) is 0:
        sceneSettings = pm.sets(name="DEX_SCENE_SETTINGS")  
        sceneSettings.hiddenInOutliner.set(True)  
        sceneSettings.addAttr("ExportLocation", dataType="string")
        sceneSettings.ExportLocation.set(".")
    else:
        sceneSettings = settingsNodes[0]
    
    return sceneSettings




def Create(newSetName, assetType=None):
    if assetType is None:
        assetType = AssetTypes.StaticMesh

    # use selected items if there is a selection
    newSet = pm.sets(name=(newSetName + "_EXPORT"))
    newSet.hiddenInOutliner.set(True)
    
    newSet.addAttr("ExportLocation", dataType="string")
    newSet.addAttr("ExportFilename", dataType="string")

    newSet.addAttr("AssetType", dataType="string")

    newSet.ExportFilename.set(newSetName + ".fbx")
    newSet.ExportLocation.set(".")
    newSet.AssetType.set(assetType.stringId)
    newSet.AssetType.lock()

    assetHandler = GetHandlerForSet(newSet)
    assetHandler.InitializeSet()

    return newSet


def Export(theSet):
    assetHandler = GetHandlerForSet(theSet)

    if assetHandler.ValidateForExport():
        assetHandler.SetFBXOptions()
        assetHandler.ApplyFBXOptions()

        assetHandler.PreExport()
        assetHandler.Export()
        assetHandler.PostExport()


def GetAssets(AssetType=None):
    if AssetType is None:
        return [a for a in pm.ls(type="objectSet") if a.hasAttr("AssetType")]
    else:
        return [a for a in pm.ls(type="objectSet") if
                a.hasAttr("AssetType") and a.AssetType.get() == AssetType.stringId]

def GetAsset(assetName):
    assets = [a for a in pm.ls(type="objectSet") if a.hasAttr("AssetType")]
    asset = [a for a in assets if a.nodeName() == assetName]
    
    if asset is not None:
        if len(asset) is not 0:
            return asset[0]
    
    return None
