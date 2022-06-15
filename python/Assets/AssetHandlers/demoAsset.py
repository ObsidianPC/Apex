verbose = False
if verbose:
    print("> demoAsset loading")

from baseAsset import baseAsset

class demoAsset( baseAsset ):

    def __init__(self, exportSet):
        super(demoAsset, self).__init__(exportSet)
        print "demoAsset constructor"

    def SetFBXOptions(self):
        super(demoAsset, self).SetFBXOptions()
        if verbose: print("--> demoAsset is setting FBX options!")


    def ApplyFBXOptions(self):
        super(demoAsset, self).ApplyFBXOptions()
        if verbose: print("--> demoAsset asset is applying FBX settings")

    def PreExport(self):
        super(demoAsset, self).PreExport()
        if verbose: print("--> demoAsset asset pre export step!")


    def GetOutputFile(self):
        return super(demoAsset, self).GetOutputFile()

    def Export(self):
        super(demoAsset, self).Export()
        if verbose: print("--> demoAsset asset pre export step!")

    def PostExport(self):
        super(demoAsset, self).PostExport()
        if verbose: print("--> demoAsset asset post export step!")