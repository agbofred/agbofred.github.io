"""
File: arraybag.py
"""
from arrays import Array
class ArrayBag(object):
    """An array-based bag implementation."""
    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it’s present."""
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
                
    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
        
    def __len__(self):
        """Returns the number of items in self."""
        return self.size
    
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
    
    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        self.items[len(self)] = item
        self.size += 1
        
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1
            
    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"  
        # possible to use [] to wrap the collection instead of {} which is a set notation
    
    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result
    
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
            len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True
    
    def count(self, item):
        """Returns the number of times item appears in self."""
        count = 0
        for element in self:
            if element == item:
                count += 1
        return count
    
    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        postcondition: item is removed from self."""
        # 1. check precondition and raise an exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # 2. Search for index of target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # 3. Shift items to the right of target left by one position
        for i in range(targetIndex, len(self) - 1):
            self.items[i] = self.items[i + 1]
        # 4. Decrement logical size
        self.size -= 1
        # 5. Check array memory here and decrease it if necessary