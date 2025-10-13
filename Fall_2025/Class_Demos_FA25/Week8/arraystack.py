from arrays import Array
from abstractstack import AbstractStack

class ArrayStack(AbstractStack):
    "Array-based stack collections"
    
    # Array inital capacity
    DEFAULT_CAPACITY = 10
    
    #Constructor
    """Initializes the state of self which include any items from sourcecollector"""
    def __init__(self, sourceCollection = None):
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)
    
    # Accessors 
    def __iter__(self):
        """Supports iteration over self. Visits items bottom to top of stack"""
        cursor =0
        while cursor < len(self):
            yield self.items[cursor]
            cursor +=1
    
    def peek(self):
        if self.isEmpty():
            raise KeyError("The stack is empty") 
        return self.items[len(self)-1]
    
    # Mutator functions
    
    def push(self, item):
        #resizing the array here if neccesary
        if self.size == len(self):
            temp = Array(len(self)+1)
            for i in range (self.size):
                temp[i] = self.items[i]
            self.items = temp  
        self.items[len(self)] = item
        self.size +=1
        
    def clear(self):
        self.size =0
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)
        
    def pop(self):
        #Check the precondition that the stack is not empty
        if self.isEmpty():
            raise KeyError("The stack is empty") 
        oldItem = self.items[len(self)-1]
        self.size -=1
        # resize the Array here if necessary
        # temp = Array(len(self)-1)
        # for i in range(self.size):
        #     temp[i] == self.items[i]
        # self.items = temp
        return oldItem