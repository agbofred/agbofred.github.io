"""
File: treesorteddict.py
Project 11.9
 Completes the tree-based sorted dictionary.
"""
from abstractdict import AbstractDict, Entry
from linkedbst import LinkedBST

class TreeSortedDict(AbstractDict):
    """Represents a tree-based sorted dictionary."""
     # Uses composition, where the dictionary contains a tree object.
    # The tree contains items, each of which contains a key and a value.
    # Each dictionary method calls the corrseponding method on the tree.
    def __init__(self, keys = None, values = None):
        """Will copy items to the collection from sourceDictionary
        if it's present."""
        self.items = LinkedBST()
        AbstractDict.__init__(self, keys, values)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return self.items.isEmpty()
    
    """Remove and inherit from parent"""
    def __len__(self):
        """-Returns the number of items in self."""
        return len(self.items)

    """Remove and inherit from parent"""
    def __str__(self):
        """Returns the string representation of self."""
        return " {" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        return self.items.inorder()

    """Remove and inherit from parent"""
    def __add__(self, other):
        """Returns a new set containing the contents
        of self and other."""
        result = type(self)(self)
        for item in self:
            result.add(item)
        return result

     # Accessors
    def __contains__(self, key):
        """Returns True if key is in self or False otherwise."""
        item = Entry(key, None)
        return item in self.items
    def __iter__(self):
        """Serves up the keys in the dictionary."""
        return map(lambda item: item.key, self.items.inorder())
    
    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        if not key in self: raise KeyError("Missing: " + str(key))
        item = Entry(key, None)
        return self.items.find(item).value
     # Mutators
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = LinkedBST()

    def __setitem__(self, key, value):
        """If the key is in the dictionary,
        replaces the old value with the new value.
        Othwerise, adds the key and value to it."""
        item = Entry(key, value)
        if key in self:
            self.items.replace(item, item)
        else:
            self.items.add(item)
            self.size += 1
    def pop(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Removes the key and returns the associated value if the
        key in in the dictionary."""
        if not key in self:
            raise KeyError("Missing: " + str(key))
        item = self.items.remove(Entry(key, None))
        self.size -= 1 
        return item.value