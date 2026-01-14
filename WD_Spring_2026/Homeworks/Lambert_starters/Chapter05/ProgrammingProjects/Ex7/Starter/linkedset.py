"""
Project 5.7
File: linkedset.py
Author: Ken Lambert
"""

from node import Node

class LinkedSet(object):
    """A link-based set implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
       
    
    def __len__(self):
        """-Returns the number of items in self."""
       

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
        

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        

    def add(self, item):
        """Adds item to self."""
        

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        
        # Search for the node containing the target item
        # probe will point to the target node, and trailer
        # will point to the one before it, if it exists
        
        # Unhook the node to be deleted, either the first one or one
        # thereafter
        
        # Decrement logical size
        
        
        
