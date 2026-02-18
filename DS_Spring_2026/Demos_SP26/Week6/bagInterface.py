"""
File: baginterface.py
"""

class BagInterface(object):
    """Interface for all bag types."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it’s present."""
        pass

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0,
        or False otherwise."""
        return True

    def __len__(self):
        """Returns the number of items in self."""
        return 0

    def __str__(self):
        """Returns the string representation of self."""
        return ""

    def __iter__(self):
        """Supports iteration over a view of self."""
        return None
    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        return None

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        return False
    
    def count(self, item):
        """Returns the number of instances of item in self."""
        return 0

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass

    def add(self, item):
        """Adds item to self."""
        pass

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        pass
    
    
    ################################# INTERFACE VERSION 2 ######################################
    
    """
FIle: bagInterface.py 
An interface that documents the class implementation for the bag interfacc
"""

class BagInterface(object):
    "Interface for all bag types"
    
    # Constructor
    def __init__(self, sourseCollector= None) -> None :
        """ 
        Sets the initial state of self, which includes the contents of sourceCollection, if
        it exists 
        """
        pass
    
    # Accessors methods
    
    def isEmpty(self) -> bool:
        """
        This is a method that checks if len(self) == 0
        then returns True. Otherwise, it returns false
            
        """
        return True
        
    def __len__(self) -> int:
        """
        Method returns the number of items in self.
        """
        return 0
    
    def __str__(self) -> str:
        """
        Method returns string representative of self
        """
        return str
    
    def __iter__(self) ->None:
        """
        Method supports iteration over a view of self 
        
        """
        return None
    
    def __add__(self, other) ->None:
        """
        Method returns a new bag containing the contents of self and other.
        """
        return None
    
    def __eg__(self, other) -> bool:
        """
        Returns True if self equals other.
        Otherwise, returns False.
        """
        return True
    
    def count(self, item) -> int:
        """This method returns the number of items in self collection"""
        return 0
    
    # Mutator methods
    
    def add(self, item):
        """Method that add new item to the end of self"""
        pass
    
    def remove(self, item):
        """
        Method that remove item from self.
        Precondition: item is in self
        Raises KeyError exception if item is not in self.
        Postcondition: item is removed from self.
        """
        
        pass