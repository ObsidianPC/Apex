from maya.cmds import about
from maya.OpenMaya import *
from maya.OpenMayaAnim import *

try:
    from maya.OpenMayaCloth import *
except:
    pass

try:
    from maya.OpenMayaFX import *
except:
    pass
try:
    from maya.OpenMayaMPx import *
except:
    pass

if not about(batch=True):
    try:
        from maya.OpenMayaUI import *
    except:
        pass

try:
    from maya.OpenMayaRender import *
except:
    pass


# fast convenience tests on API objects
def isValidMObjectHandle(obj):
    if isinstance(obj, MObjectHandle):
        return obj.isValid() and obj.isAlive()
    else:
        return False


def isValidMObject(obj):
    if isinstance(obj, MObject):
        return not obj.isNull()
    else:
        return False


def isValidMPlug(obj):
    if isinstance(obj, MPlug):
        return not obj.isNull()
    else:
        return False


def isValidMDagPath(obj):
    if isinstance(obj, MDagPath):
        return obj.isValid()
    else:
        return False


def isValidMNode(obj):
    if isValidMObject(obj):
        return obj.hasFn(MFn.kDependencyNode)
    else:
        return False


def isValidMDagNode(obj):
    if isValidMObject(obj):
        return obj.hasFn(MFn.kDagNode)
    else:
        return False


def isValidMNodeOrPlug(obj):
    return isValidMPlug(obj) or isValidMNode(obj)


# Converting API MObjects and more

# returns a MObject for an existing node
def toMObject(nodeName):
    """ Get the API MObject given the name of an existing node """
    sel = MSelectionList()
    obj = MObject()
    result = None
    try:
        sel.add(nodeName)
        sel.getDependNode(0, obj)
        if isValidMObject(obj):
            result = obj
    except:
        pass
    return result


def toMDagPath(nodeName):
    """ Get an API MDagPAth to the node, given the name of an existing
dag node """
    obj = toMObject(nodeName)
    if isValidMDagNode(obj):
        dagFn = MFnDagNode(obj)
        dagPath = MDagPath()
        dagFn.getPath(dagPath)
        return dagPath


# returns a MPlug for an existing plug
def toMPlug(plugName):
    """ Get the API MObject given the name of an existing plug
(node.attribute) """
    nodeAndAttr = plugName.split('.', 1)
    obj = toMObject(nodeAndAttr[0])
    plug = None
    if isValidMObject(obj):
        depNodeFn = MFnDependencyNode(obj)
        attr = depNodeFn.attribute(nodeAndAttr[1])
        plug = MPlug(obj, attr)
        if plug.isNull():
            plug = None
    return plug


# MDagPath, MPlug or MObject to name
# Note there is a kNamedObject API type but not corresponding MFn, thus
# I see no way of querying the name of something that isn't a kDependency
# node or a MPlug


# TODO : add components support, short/ long name support where applies
def MObjectName(obj):
    """ Get the name of an existing MPlug, MDagPath or MObject
representing a dependency node"""
    if isValidMPlug(obj):
        return obj.name()
    elif isValidMNode(obj):
        depNodeFn = MFnDependencyNode(obj)
        return depNodeFn.name()
    elif isValidMDagPath(obj):
        # return obj.fullPathName()
        return obj.partialPathName()
    else:
        return unicode(obj)