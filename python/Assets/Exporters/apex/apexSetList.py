import Assets.UIWidgets.setListWidget as setListWidget
reload(setListWidget)
import pymel.core as pm

class dexSetList(setListWidget.setList):
    def __init__(self):
        super(dexSetList, self).__init__()       
        self.customizeItemDelegate = None
    
    def insertItem(self, item, parent, index, bHideButtons=False):
        super(dexSetList, self).insertItem(item, parent, index, bHideButtons=bHideButtons)

        if self.customizeItemDelegate is not None:
            self.customizeItemDelegate(item, parent)

    def addItem(self, item, parent="", bHideButtons=False):
        super(dexSetList, self).addItem(item, parent, bHideButtons=bHideButtons)
        
        if self.customizeItemDelegate is not None:
            self.customizeItemDelegate(item, parent)
    
        
def createSetList():
    sl = dexSetList()
    return sl
    
    