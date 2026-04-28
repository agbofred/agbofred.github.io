"""
File: linkedbst.py
Author: Ken Lambert
"""
from week16.abstractcollection import AbstractCollection
from bstnode import BSTNode

class LinkedBST (AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.root = None
        AbstractCollection.__init__(self, sourceCollection)

        # Implement add, remove, find, __contains__, __iter__, etc.