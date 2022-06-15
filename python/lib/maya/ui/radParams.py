import pymel.core as pm
import sys
from event import *
from weakref import WeakKeyDictionary

class ParamWrapper(object):
    '''This is a wrapper for a basic parameter.  The intention is for this wrapper to also
    contain an event that can be subscribed to and consumed from many places at once.'''
    def __init__(self, defaultValue=0.0):
        self.val = defaultValue
        self.data = WeakKeyDictionary()
        self.callbacks = WeakKeyDictionary()

    def __get__(self, instance, owner):
        '''This is the get docstring'''
        #Define behavior for when the descriptor's value is retrieved.
        #instance is the instance of the owner object. owner is the owner class itself.
        if instance is None:
            return self

        return self.data.get(instance, self.val)

    def __set__(self, instance, value):
        '''This is the set docstring'''
        #Define behavior for when the descriptor's value is retrieved.
        #instance is the instance of the owner object.
        self.data[instance] = value
        for callback in self.callbacks.get(instance, []):
            callback(value)

    def addCallback(self, instance, callback):
        """Add a new function to call everytime the descriptor within instance updates"""
        if instance not in self.callbacks:
            self.callbacks[instance] = list()

        self.callbacks[instance].append(callback)


class ListParamWrapper( object ):

    def __init__(self, values=None):
        if values is None:
            self.values = list()
        else:
            self.values = values

        self.onListChange = Event()


    def __len__(self):
        #Returns the length of the container. Part of the protocol for both
        #immutable and mutable containers.
        return len(self.values)

    def __getitem__(self, index):
        #Defines behavior for when an item is accessed, using the notation
        #self[key]. This is also part of both the mutable and immutable
        #container protocols. It should also raise appropriate exceptions:
        #TypeError if the type of the key is wrong and KeyError if there is
        #no corresponding value for the key.
        return self.values[index]

    def __setitem__(self, index, value):
        #Defines behavior for when an item is assigned to, using the
        #notation self[nkey] = value. This is part of the mutable container
        #protocol. Again, you should raise KeyError and TypeError where appropriate.
        self.values[index] = value
        self.onListChange.fire(self.values)

    def __delitem__(self, index):
        #Defines behavior for when an item is deleted (e.g. del self[key]).
        #This is only part of the mutable container protocol. You must raise
        # the appropriate exceptions when an invalid key is used.
        del self.values[index]
        self.onListChange.fire(self.values)

    def __iter__(self):
        #Should return an iterator for the container. Iterators are returned in
        #a number of contexts, most notably by the iter() built in function and
        #when a container is looped over using the form for x in container:.
        #Iterators are their own objects, and they also must define an
        #__iter__ method that returns self.
        return iter(self.values)


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


    def append(self, value):
        self.values.append(value)
        self.onListChange.fire(self.values)

    def extend(self, valueList):
        self.values.extend(valueList)
        self.onListChange.fire(self.values)

    def remove(self, value):
        self.values.remove(value)
        self.onListChange.fire(self.values)

    def index(self, value):
        return self.values.index(value)