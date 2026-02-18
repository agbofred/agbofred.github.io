from arrays import Array
from abstractqueue import AbstractQueue

class ArrayQueue(AbstractQueue):
    "Array-based queue collections"
    
    # Array inital capacity
    DEFAULT_CAPACITY = 10
    
    #Constructor
    """Initializes the state of self which include any items from sourcecollector"""
    def __init__(self, sourceCollection = None):
        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)
        # We must inititalize the front and rear variables to also use them to trace the pop and add
        self.front = -1
        self.rear = -1
        AbstractQueue.__init__(self, sourceCollection)
    
    # Accessors 
    def __iter__(self):
        """Supports iteration over self. Visits items bottom to top of stack"""
        cursor = self.front
        while cursor !=self.rear:
            yield self.items[cursor]
            if cursor == len(self.items)-1:
                cursor = 0
            else:
                cursor += 1
        if cursor == self.rear and cursor != -1:
            yield self.items[cursor]
    
    def peek(self):
        if self.isEmpty():
            raise KeyError("The Queue is empty") 
        return self.items[self.front]
    
    # Mutator functions
        
    def add(self, item):
        #resizing the array here if neccesary
        if len(self) == len(self.items):
            temp = Array(len(self.items) *2)
            for i in range (self.size):
                temp[i] = self.items[i]
            self.items = temp  
            if not self.isEmpty():
                self.front = 0
                self.rear = len(self) - 1
        if self.isEmpty():
            self.front = self.rear = 0
        elif self.rear == len(self.items) - 1:
            self.rear = 0
        else:
            self.rear += 1  
        self.items[self.rear] = item
        self.size +=1
        
    def clear(self):
        self.size =0
        self.front = self.rear = -1
        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)
        
    def pop(self):
        #Check the precondition that the stack is not empty
        if self.isEmpty():
            raise KeyError("The stack is empty") 
        oldItem = self.items[self.front]
        self.size -= 1
        # resize the Array here if necessary
        if self.isEmpty():
            self.front = self.rear = -1
        elif self.front == len(self.items) - 1:
            self.front = 0
        else:
            self.front += 1
        if len(self) <= 0.25 * len(self.items) \
            and ArrayQueue.DEFAULT_CAPACITY <= len(self.items) //2:
            temp = Array(len(self.items)// 2)
            i = 0
            for item in self:
                temp[i] = item
                i +=1
            self.items = temp
            if not self.isEmpty():
                self.front = 0
                self.rear = len(self) -1
        return oldItem