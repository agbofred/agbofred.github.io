"""
File: linkedstack.py
Author: Ken Lambert
"""

from node import Node
from abstractstack import AbstractStack

class LinkedStack(AbstractStack):
    """A link-based stack implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        
        def visitNodes(node):
            """Adds items to tempList from tail to head."""
            

    def peek(self):
        """
        Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if the stack is empty."""
        if self.isEmpty():
            

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        

    def push(self, item):
        """Adds item to the top of the stack."""
        

    def pop(self):
        """
        Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if the stack is empty.
        Postcondition: the top item is removed from the stack."""
               
        
