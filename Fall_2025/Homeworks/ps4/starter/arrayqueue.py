from abstractqueue import AbstractQueue
from arrays import Array

class ArrayQueue(AbstractQueue):
    """Array-based queue collection (template)."""
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        # Initialize the array and front/rear pointers
        pass

    def __iter__(self):
        """Iterate over the queue from front to rear."""
        pass

    def peek(self):
        """Return the item at the front without removing it."""
        pass

    def add(self, item):
        """Add an item to the rear of the queue."""
        pass

    def pop(self):
        """Remove and return the item at the front of the queue."""
        pass

    def clear(self):
        """Remove all items from the queue."""
        pass

# Worksheet Prompts (for students):
# 1. Complete the ArrayQueue class by implementing all methods above.
# 2. Use the ArrayStack implementation as a guide for array resizing and index management.
# 3. Ensure your queue supports circular array behavior for efficient use of space.
# 4. Your instructor will provide a testqueue.py file to test your implementation.
# 5. After implementation, write a short comment comparing the time and space complexity (Big O) of ArrayQueue and LinkedQueue for all major operations.
