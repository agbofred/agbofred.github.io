"""
File: treesortedset.py

Project 10.6

A binary search tree-based implementation of a sorted set.
"""

from linkedbst import LinkedBST
from abstractbag import AbstractBag

class TreeSortedSet(AbstractBag):
    """A binary search tree-based implementation of a sorted set."""

    # Uses a LinkedBST to contain the set's items.
    # The tree is rebalanced after items are added during istantiation.
    # The iterator uses an inorder traversal to ensure visiting items
    # in ascending order.

    # eq is overridden for set-specific equality.

    # Searches, insertions, and removals are logarithmic on average,
    # and linear in the worst case.

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
    

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
    

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

        
