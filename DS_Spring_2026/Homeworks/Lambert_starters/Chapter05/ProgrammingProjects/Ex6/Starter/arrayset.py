"""
Project 5.6
File: arrayset.py
Author: Ken Lambert
"""

from arrays import Array

class ArraySet(object):
    """An array-based set implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = Array(ArraySet.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
    
    def __len__(self):
        """Returns the number of items in self."""
        

    def __str__(self):
        """Returns the string representation of self."""

        
    def __iter__(self):
        """Supports iteration over a view of self."""
        

    def __add__(self, other):
        """Returns a new set containing the contents
        of self and other."""
        

    def clone(self):
        """Returns a copy of self."""
        

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        

    def count(self, item):
        """Returns the number of instances of item in self."""
        

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        

    def add(self, item):
        """Adds item to self."""
        if not item in self:
            # Check array memory here and increase it if necessary
            

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        
        # Search for the index of the target item
        
        # Shift items to the left of target up by one position
        
        # Decrement logical size
        
        # Check array memory here and decrease it if necessary
        
       
        
