verbose = False
if verbose:print("> skinnedMeshAsset loading")

import baseAsset

class skinnedMeshAsset(baseAsset.baseAsset):
    stringId = "skinnedMeshAsset"
    
    def __init__(self, exportSet):
        super(skinnedMeshAsset, self).__init__(exportSet)
        if verbose:print "skinnedMeshAsset constructor"
        self.stringId = "skinnedMeshAsset"

    def SetFBXOptions(self):
        super(skinnedMeshAsset, self).SetFBXOptions()
        if verbose:print "Setting skinnedMeshAsset FBX Settings"

        self.settings['Export|IncludeGrp|Animation|Deformation']['VALUE'] = "true"
        self.settings['Export|IncludeGrp|Animation|Deformation|Skins']['VALUE'] = "true"        
        self.settings['Export|AdvOptGrp|UnitsGrp|UnitsSelector']['VALUE'] = "Meters"

        self.settings['Export|IncludeGrp|Animation']['VALUE'] = "false"
        
