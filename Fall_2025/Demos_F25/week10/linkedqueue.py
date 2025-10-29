from node import Node
from abstractqueue import AbstractQueue

class LinkedQueue(AbstractQueue):
    """ Link-based queue implementation."""
    def __init__(self, sourceCollection = None):
        self.front = self.rear = None
        AbstractQueue.__init__(self, sourceCollection)
        
    # Accessors
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.front
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next
    
    def peek(self):
        """Returns the item at top of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self.front.data
    
    # Mutators
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.front = self.rear = None
        
    def add(self, item):
        """Inserts item at top of the queue."""
        newNode = Node(item, None)
        if self.isEmpty():
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.size += 1
        
    def pop(self):
        """Removes and returns the item at top of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        self.size -= 1
        return oldItem