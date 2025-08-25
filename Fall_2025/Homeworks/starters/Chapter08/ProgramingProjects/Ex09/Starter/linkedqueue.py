"""
File: linkedqueue.py
Project 8.9
"""

from node import Node
from abstractcollection import AbstractCollection

class LinkedQueue(AbstractCollection):
    """A link-based queue implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self,
        which includes the contents of
        sourceCollection, if it's present."""
        # Write your code below:

    # Accessor methods
    def __iter__(self):
        """Supports iteration
        over a view of self."""
        # Write your code below:
        
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the stack is empty."""
        # Write your code below:

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        # Write your code below:

    def add(self, item):
        """Adds item to the rear of the queue."""
        # Write your code below:

    def pop(self):
        """Removes and returns the item
        at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the queue is empty.
        Postcondition: the front item is
        removed from the queue."""
        # Write your code below:
        
