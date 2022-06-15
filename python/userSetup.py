"""
Maya Bootup Script
"""

import pymel.core as pm
import maya.cmds as cmds
import os
import subprocess
import Settings

import maya.utils as mtutil

verbose = True

def getLocation():
    location = pm.mel.eval("whatIs userSetup")
    location = location.replace("Script found in: ", "")
    location = location.replace("/scripts/userSetup.mel", "")
    location = os.path.normpath(location)
    return location

def apexMayaLaunch():
    print("Starting Apex Python UserSetup")
    location = getLocation()

    CLEAR_PYCACHE_AT_STARTUP = Settings.CLEAR_PYCACHE_AT_STARTUP.value

    if CLEAR_PYCACHE_AT_STARTUP:
        print("Cleaning Apex cached python code...")
        pycLocation = os.path.normpath(location + "/python/*.pyc")
        try:
            res = subprocess.check_output(["del", pycLocation, "/S"], shell=True)
            if verbose: 
                print res
        except subprocess.CalledProcessError as err:
            print "Problem clearing out python cache: " + str(err)


    
    import Shelves.apexShelf
    

mtutil.executeDeferred(apexMayaLaunch)
