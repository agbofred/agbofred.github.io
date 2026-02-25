
from node import Node
from abstractstack import AbstractStack

class LinkedStack(AbstractStack):
    """ Link-based stack implementation."""
    def __init__(self, sourceCollection = None):
        self.items = None
        AbstractStack.__init__(self, sourceCollection)
        
    # Accessors
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        tempList = list()
        def visitNodes(node):
            if node != None:
                visitNodes(node.next)
                tempList.append(node.data)
        visitNodes(self.items)
        return iter(tempList)
    
    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        return self.items.data
    
    # Mutators
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = None
        
    def push(self, item):
        """Inserts item at top of the stack."""
        self.items = Node(item, self.items)
        self.size += 1
        
    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        oldItem = self.items.data
        self.items = self.items.next
        self.size -= 1
        return oldItem
    
    def add(self, item):
        """Adds item to the stack."""
        self.push(item)