# towerofhanoi.py
########################################
# Your Name:
# Indicate any collaborators or tools used to assist you including AI:
# Estimated time spent (hrs):
########################################

from arraystack import ArrayStack

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