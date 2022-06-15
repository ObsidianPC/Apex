import pymel.core as pm

#use this prefix on options please
DEFAULT_OPTION_PREFIX = "_APEX_"  #TODO:  Enforce this somehow - wrapper methods, magic methods, etc.


def GetArtToolRoot():
    userScriptLocation = pm.mel.eval('whatIs userSetup')
    userScriptLocation = userScriptLocation.replace("Script found in: ", "")
    userScriptLocation = userScriptLocation.replace("scripts/userSetup.mel", "")
    return userScriptLocation 


class ToolSetting(object):
    def __init__(self, name, defaultValue=None):
        self.name = name
        self.defaultValue = defaultValue
        
        if (pm.optionVar.has_key(name) == True):
            self.value = pm.optionVar[name]
        else:
            self.value = defaultValue


CLEAR_PYCACHE_AT_STARTUP    = ToolSetting("_APEX_CLEAR_PYCACHE_AT_STARTUP", defaultValue=True)
AJH_DEBUG_ENABLE            = ToolSetting("_APEX_DEBUG_ENABLE", defaultValue=False)



ARTTOOL_ROOT                = ToolSetting("_APEX_ARTTOOL_ROOT", defaultValue=GetArtToolRoot())