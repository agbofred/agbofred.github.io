# # def solvemaze(maze,x,y, path):
# #     #base case
# #     if maze[x][y]=="E":
# #         path.append((x,y))
# #         return True
# #     maze[x][y] = "#"
# #          # Move right, down, up, left
# #     moves = [(0,1),(1,0),(-1,0),(0,-1)]
# #     for dx, dy in moves:
# #         nx, ny, = x + dx, y + dy
# #         if 0<= nx <len(maze) and 0<= ny <len(maze[0]) and maze[nx][ny] in (' ', 'E'):
# #             if solvemaze(maze, nx, ny, path):
# #                 path.append((x,y))
# #                 return True
# #     return False 
                
# # maze = [['S', ' ', '#'],
# #         [' ', ' ', 'E']
# #         ]
# # maze2= [
# #     ['S', ' ', ' ', ' ', ' ', ' ', ' '],
# #     ['#', '#', ' ', '#', ' ', '#', ' '],
# #     [' ', ' ', ' ', ' ', ' ', '#', ' '],
# #     [' ', '#', '#', '#', ' ', '#', ' '],
# #     [' ', ' ', ' ', '#', ' ', ' ', 'E']
# # ]
# # path =[]
# # solvemaze(maze2, 0,0, path)
# # print(f"Path to the exit are: ", path[::-1])

# print(f"{(2**64)-1}")

# Pythonic function-based ToH 
def create_tower_of_hanoi(n_disks=3):
    stacks = [[] for _ in range(3)]
    labels = ['L', 'M', 'R']
    # Initialize first spindle with disks in descending order
    stacks[0] = list(range(n_disks, 0, -1))
    return stacks, labels

def reset_tower(stacks, n_disks):
    for spindle in range(3):
        stacks[spindle] = []
    stacks[0] = list(range(n_disks, 0, -1))

def label(labels, spindle):
    return labels[spindle]
# Lenght of each rod = number of disk on a spindle
def height(stacks, spindle):
    return len(stacks[spindle])

def top_disk(stacks, spindle):
    if stacks[spindle]:
        return stacks[spindle][-1]
    return None
#Create the tower
def tower_str(stacks, labels):
    result = ""
    for spindle in range(3):
        if result:
            result += "\n"
        result += f"{labels[spindle]}: {stacks[spindle]}"
    return result

## ToH movement
def move(stacks, labels, source, to, show=False):
    if not stacks[source]:
        raise Exception("Cannot move from empty spindle " + labels[source])
    if stacks[to] and stacks[source][-1] > stacks[to][-1]:
        raise Exception(
            "Cannot move disk " + str(stacks[source][-1]) +
            " on top of disk " + str(stacks[to][-1])
        )
    disk = stacks[source].pop()
    stacks[to].append(disk)
    if show:
        print('Move disk', disk, 'from spindle', labels[source], 'to', labels[to])

## Recursive function 'Solve'
def solve(stacks, labels, n_disks=None, start=0, goal=2, spare=1, show=False, total_disks=None):
    if n_disks is None:
        n_disks = len(stacks[start])
    if total_disks is None:
        total_disks = n_disks
    if n_disks <= 0:
        return
    if len(stacks[start]) < n_disks:
        raise Exception(
            "Not enough disks (" + str(n_disks) +
            ") on starting spindle " + labels[start]
        )
    ## Recursive call
    solve(stacks, labels, n_disks - 1, start, spare, goal, show, total_disks)
    move(stacks, labels, start, goal, show)
    if show:
        print(tower_str(stacks, labels))
    solve(stacks, labels, n_disks - 1, spare, goal, start, show, total_disks)
    if n_disks == total_disks and show:
        print("Puzzle complete")

# Example usage:
n_disks = 3
stacks, labels = create_tower_of_hanoi(n_disks)
print(tower_str(stacks, labels))
solve(stacks, labels, show=True)