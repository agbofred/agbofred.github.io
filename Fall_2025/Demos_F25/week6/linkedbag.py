"""
File: linkedbag.py
"""
from node import Node

class LinkedBag(object):
    """A link-based bag implementation."""
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it’s present."""
        self.items = None
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
                
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.items
        while cursor != None:
            yield cursor.data
            cursor = cursor.next
    def add(self, item):
        """Adds item to self."""
        self.items = Node(item, self.items)
        self.size += 1
    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise an exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the node containing the target item
        # probe will point to the target node, and trailer
        # will point to the node before it, if it exists
        probe = self.items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        # Unhook the node to be deleted, either the first one or 
        # one thereafter
        if probe == self.items:
            self.items = self.items.next
        else:
            trailer.next = probe.next
        # Decrement logical size
        self.size -= 1
