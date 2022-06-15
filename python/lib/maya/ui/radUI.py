import pymel.core as pm
import sys
from event import *

class radOptionMenuGrp( pm.uitypes.OptionMenuGrp ):

    @classmethod
    def _preCreateVirtual(cls, **kwargs ):
        """This is called before creation. python allowed."""
        print "preCreateVirtual"
        return kwargs

    @classmethod
    def _postCreateVirtual(cls, newNode ):
        """ This is called after creation, pymel/cmds allowed. Treat newNode as self."""
        print "postCreateVirtual"

    def setAllItems(self, newItemLabelArray, bRememberSelection=True):

        currentSelection = self.getValue()

        for item in self.getItemListLong():
            pm.deleteUI(item)

        self.addMenuItems(newItemLabelArray)

        if bRememberSelection:
            if currentSelection in self:
                self.setValue(currentSelection)


    def removeItem(self, label):
        if self.indexForLabel(label) != None:
            del self[self.indexForLabel(label)]

    def removeItemAtIndex(self, index):
        del self[index]

    def replaceItemLabel(self, oldLabel, newLabel):
        items = self.getItemListLong()

        for item in items:
            itemLabel = pm.menuItem(item, query=True, label=True)

            if itemLabel == oldLabel:
                pm.menuItem(item, edit=True, label=newLabel)

    def indexForLabel(self, label):
        items = self.getItemListLong()

        for item in items:
            itemLabel = pm.menuItem(item, query=True, label=True)

            if itemLabel == label:
                return items.index(item)

        return None

    def __len__(self):
        #Returns the length of the container. Part of the protocol for both
        #immutable and mutable containers.
        return self.getNumberOfItems()

    def __getitem__(self, index):
        #Defines behavior for when an item is accessed, using the notation
        #self[key]. This is also part of both the mutable and immutable
        #container protocols. It should also raise appropriate exceptions:
        #TypeError if the type of the key is wrong and KeyError if there is
        #no corresponding value for the key.
        item = self.getItemListLong()[index]
        itemLabel = pm.menuItem(item, query=True, label=True)
        return itemLabel

    def __setitem__(self, index, newLabel):
        #Defines behavior for when an item is assigned to, using the
        #notation self[nkey] = value. This is part of the mutable container
        #protocol. Again, you should raise KeyError and TypeError where appropriate.
        items = self.getItemListLong()
        item = items[index]
        pm.menuItem(item, edit=True, label=newLabel)

    def __delitem__(self, index):
        #Defines behavior for when an item is deleted (e.g. del self[key]).
        #This is only part of the mutable container protocol. You must raise
        # the appropriate exceptions when an invalid key is used.
        items = self.getItemListLong()

        selectedItem = self.getSelect() - 1

        if (selectedItem == index):
            self.setSelect(1)

        pm.deleteUI(items[index])

    def __contains__(self, label):
        #__contains__ defines behavior for membership tests using in and
        #not in. Why isn't this part of a sequence protocol, you ask?
        #Because when __contains__ isn't defined, Python just iterates over
        #the sequence and returns True if it comes across the item it's
        #looking for.
        items = self.getItemListLong()

        for item in items:
            itemLabel = pm.menuItem(item, query=True, label=True)

            if itemLabel == label:
                return True

        return False

    def __del__(self):
        #clean up event ids here!
        pass
