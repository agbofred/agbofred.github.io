class StackInterface(object):
    """This interface is for all Stacks type"""
    
    
    #Contructor
    def __init__(self, sourceCollection =None):
        """Sets the initial state of self, wich includes contents of the 
        sourceCOllection if its present"""
        pass
                
    def isEmpty(self):
        """Returns True if stack is empty. Otherwise, returns False 
        """
        return True
    
    def __len__(self):
        """Returns the number of items in stack
        """
        return 0
    
    def __str__(self):
        """Returns the string repsentative of S
        """
        return ""
    
    def contains(self, item):
        """Returns True is items is in stack or False otherwise
            This is essentially the same as item in s
        """
        pass
    
    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        pass

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        return True
    
    def clear(self):
        """Make stack become empty"""
        pass
    
    def peek(self):
        """Returns the item at the top of stack. Precondition is that stack must not be empty"""
        pass
    
    def push(self, item):
        """adds item to the top of stack """
        pass
        
    def pop(self):
        """Remove an item from the top of the stack """
        pass

                