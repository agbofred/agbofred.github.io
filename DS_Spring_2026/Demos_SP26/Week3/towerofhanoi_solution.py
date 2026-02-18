class ArrayStack:
    """
    Stack implementation using an array (fixed-size, no Python list stack methods).
    """
    def __init__(self, capacity):
        self._array = [None] * capacity
        self._capacity = capacity
        self._top = -1

    def push(self, item):
        if self._top + 1 >= self._capacity:
            raise Exception("Stack is full")
        self._top += 1
        self._array[self._top] = item

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        item = self._array[self._top]
        self._array[self._top] = None
        self._top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._array[self._top]

    def is_empty(self):
        return self._top == -1

    def __str__(self):
        return str([self._array[i] for i in range(self._top + 1)])

class TowerOfHanoi:
    def __init__(self, n_disks):
        self.n_disks = n_disks
        self.labels = ['L', 'M', 'R']
        self.towers = [ArrayStack(n_disks) for _ in range(3)]
        for disk in range(n_disks, 0, -1):
            self.towers[0].push(disk)

    def move(self, source, target, show=False):
        if self.towers[source].is_empty():
            raise Exception(f"Cannot move from empty spindle {self.labels[source]}")
        disk = self.towers[source].peek()
        if not self.towers[target].is_empty() and disk > self.towers[target].peek():
            raise Exception(f"Cannot move disk {disk} on top of disk {self.towers[target].peek()}")
        disk = self.towers[source].pop()
        self.towers[target].push(disk)
        if show:
            print(f"Move disk {disk} from spindle {self.labels[source]} to {self.labels[target]}")

    def print_towers(self):
        for i in range(3):
            print(f"{self.labels[i]}: {self.towers[i]}")

    def solve(self, n=None, start=0, goal=2, spare=1, show=False, total_disks=None):
        if n is None:
            n = self.n_disks
        if total_disks is None:
            total_disks = n
        if n <= 0:
            return
        if self.towers[start]._top + 1 < n:
            raise Exception(f"Not enough disks ({n}) on starting spindle {self.labels[start]}")
        self.solve(n - 1, start, spare, goal, show, total_disks)
        self.move(start, goal, show)
        if show:
            self.print_towers()
        self.solve(n - 1, spare, goal, start, show, total_disks)
        if n == total_disks and show:
            print("Puzzle complete!")

if __name__ == "__main__":
    n_disks = 5
    game = TowerOfHanoi(n_disks)
    game.print_towers()
    game.solve(show=True)
