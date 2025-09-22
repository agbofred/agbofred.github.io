class ArrayStack:
    """
    Stack implementation using an array (fixed-size, no Python list stack methods for stack ops).
    """
    def __init__(self, capacity):
        """Initialize the stack with a fixed capacity."""
        self._array = [None] * capacity
        self._capacity = capacity
        self._top = -1

    def push(self, item):
        """Push an item onto the stack. Raise exception if full."""
        pass  # TODO: Implement

    def pop(self):
        """Remove and return the top item. Raise exception if empty."""
        pass  # TODO: Implement

    def peek(self):
        """Return the top item without removing it. Raise exception if empty."""
        pass  # TODO: Implement

    def is_empty(self):
        """Return True if the stack is empty."""
        pass  # TODO: Implement

    def __str__(self):
        """Return a string representation of the stack (top at right)."""
        pass  # TODO: Implement

class TowerOfHanoi:
    """
    Tower of Hanoi game using three ArrayStack objects.
    """
    def __init__(self, n_disks):
        """Initialize the three towers and place all disks on the first tower."""
        pass  # TODO: Implement

    def move(self, source, target):
        """Move the top disk from source stack to target stack. Raise exception if invalid."""
        pass  # TODO: Implement

    def print_towers(self):
        """Print the current state of all towers."""
        pass  # TODO: Implement

    def solve(self, n=None, start=0, goal=2, spare=1, show=False):
        """Recursively solve the Tower of Hanoi puzzle."""
        pass  # TODO: Implement

if __name__ == "__main__":
    n_disks = 3
    game = TowerOfHanoi(n_disks)
    game.print_towers()
    game.solve(show=True)
    print("Puzzle complete!")
