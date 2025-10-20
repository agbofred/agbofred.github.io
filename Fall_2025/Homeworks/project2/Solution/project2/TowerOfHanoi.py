from arraystack import ArrayStack

class TowerOfHanoi:
    def __init__(self, n_disks):
        self.n_disks = n_disks
        self.labels = ['L', 'M', 'R']
        self.towers = [ArrayStack() for _ in range(3)]
        for disk in range(n_disks, 0, -1):
            self.towers[0].push(disk)

    def move(self, source, target, show=False):
        if self.towers[source].isEmpty():
            raise Exception(f"Cannot move from empty spindle {self.labels[source]}")
        disk = self.towers[source].peek()
        if not self.towers[target].isEmpty() and disk > self.towers[target].peek():
            raise Exception(f"Cannot move disk {disk} on top of disk {self.towers[target].peek()}")
        disk = self.towers[source].pop()
        self.towers[target].push(disk)
        if show:
            print(f"Move disk {disk} from spindle {self.labels[source]} to {self.labels[target]}")

    def print_towers(self):
        for i in range(3):
            print(f"{self.labels[i]}: {[item for item in self.towers[i]]}")

    def solve(self, n=None, start=0, goal=2, spare=1, show=False, total_disks=None):
        if n is None:
            n = self.n_disks
        if total_disks is None:
            total_disks = n
        if n <= 0:
            return
        if len([item for item in self.towers[start]]) < n:
            raise Exception(f"Not enough disks ({n}) on starting spindle {self.labels[start]}")
        self.solve(n - 1, start, spare, goal, show, total_disks)
        self.move(start, goal, show)
        if show:
            self.print_towers()
        self.solve(n - 1, spare, goal, start, show, total_disks)
        if n == total_disks and show:
            print("Puzzle complete!")

if __name__ == "__main__":
    n_disks = 6
    game = TowerOfHanoi(n_disks)
    game.print_towers()
    game.solve(show=True)
