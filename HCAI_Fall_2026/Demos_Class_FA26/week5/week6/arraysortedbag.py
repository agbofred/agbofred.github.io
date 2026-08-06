"""
File: arraysortedbag.py
An array-based sorted bag implementation using inheritance.
"""

from arraybag import ArrayBag

class ArraySortedBag(ArrayBag):
    """An array-based sorted bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ArrayBag.__init__(self, sourceCollection)

    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in self, or False otherwise.
        Uses binary search for O(log n) performance."""
        left = 0
        right = len(self) - 1
        while left <= right:
            midPoint = (left + right) // 2
            if self.items[midPoint] == item:
                return True
            elif self.items[midPoint] > item:
                right = midPoint - 1
            else:
                left = midPoint + 1
        return False

    # Mutator methods
    def add(self, item):
        """Adds item to self while maintaining sorted order."""
        # Empty or last item, call ArrayBag.add
        if self.isEmpty() or item >= self.items[len(self) - 1]:
            ArrayBag.add(self, item)
        else:
            # Search for first item >= new item
            targetIndex = 0
            for targetItem in self:
                if targetItem >= item:
                    break
                targetIndex += 1
            
            # Check array memory and increase if necessary
            if len(self) == len(self.items):
                from arrays import Array
                temp = Array(len(self) * 2)
                for i in range(len(self)):
                    temp[i] = self.items[i]
                self.items = temp
            
            # Open a hole for the new item
            for i in range(len(self), targetIndex, -1):
                self.items[i] = self.items[i - 1]
            
            # Insert the new item and update size
            self.items[targetIndex] = item
            self.size += 1

    def __add__(self, other):
        """Returns a new sorted bag containing the contents
        of self and other."""
        result = ArraySortedBag(self)
        for item in other:
            result.add(item)
        return result
