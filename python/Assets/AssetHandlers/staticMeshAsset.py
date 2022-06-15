verbose = True
if verbose:print("> staticMeshAsset loading")

import baseAsset

class staticMeshAsset(baseAsset.baseAsset):
    stringId = "staticMesh"
    
    def __init__(self, exportSet):
        super(staticMeshAsset, self).__init__(exportSet)
        if verbose:print "staticMeshAsset constructor"
        self.stringId = "staticMesh"

    def SetFBXOptions(self):
        super(staticMeshAsset, self).SetFBXOptions()
        if verbose:print "Setting staticMeshAsset FBX Settings"

        self.settings['Export|IncludeGrp|Animation|Deformation']['VALUE'] = "false"
        self.settings['Export|IncludeGrp|InputConnectionsGrp|InputConnections']['VALUE'] = "false"
        
        self.settings['Export|AdvOptGrp|UnitsGrp|UnitsSelector']['VALUE'] = "Meters"