import pymel.core as pm

def setOV( ):
    # set optionVars
    pm.optionVar['workingUnitLinear'] = 'cm'
    pm.optionVar['workingUnitLinearDefault'] = 'cm'
    pm.optionVar['workingUnitTime'] = 'ntsc'
    pm.optionVar['workingUnitTimeDefault'] = 'ntsc'

    # default Angular units
    pm.optionVar( sv=("workingUnitAngularDefault", "degree") )

    # default playback times
    pm.optionVar['playbackMinDefault'] = 0
    pm.optionVar( fv=('playbackMaxDefault', 60) )
    pm.optionVar( fv=('playbackMinRangeDefault', 0) )
    pm.optionVar( fv=('playbackMaxRangeDefault', 60) )

    # incremental backups
    pm.optionVar( iv=("isIncrementalSaveEnabled", 0) )
    pm.optionVar( iv=("incrementalSaveLimitBackups", 1) )
    pm.optionVar( iv=("incrementalSaveMaxBackups", 20) )

    # Recent files
    pm.optionVar( iv=("RecentFilesMaxSize", 20) )

    # tools settings
    pm.optionVar['removeReferenceEdits'] = True

    # initially set to false
    if not pm.optionVar.has_key( 'sceneValidate' ):
        pm.optionVar['sceneValidate'] = False

    # initially set to false
    if not pm.optionVar.has_key( 'p4Checkout' ):
        pm.optionVar['p4Checkout'] = False

    if not pm.optionVar.has_key( 'p4CheckoutAlways' ):
        pm.optionVar['p4CheckoutAlways'] = False

    # initially set to false
    if not pm.optionVar.has_key( 'zUp' ):
        pm.optionVar['zUp'] = False

    # # initially set to false
    # if not pm.optionVar.has_key( 'makeRelativePaths' ):
    #     pm.optionVar['makeRelativePaths'] = False

    # needed? settings
    pm.melGlobals.initVar( 'int', 'gUseScenePanelConfig' )
    pm.melGlobals.initVar( 'int', 'gUseSaveScenePanelConfig' )

    # save or load layouts from scene
    pm.mel.file( uc=True )
    pm.melGlobals['gUseScenePanelConfig'] = 0
    pm.melGlobals['gUseSaveScenePanelConfig'] = 0

    # playback realtime
    pm.playbackOptions( ps=1.0 )

    # disable 2017 mel redeclaration warning
    pm.melOptions( duplicateVariableWarnings=False )
    # print "Studio settings reset..."