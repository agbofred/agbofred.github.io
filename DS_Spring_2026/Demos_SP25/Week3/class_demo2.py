def solve_maze(maze, x, y, path):
    # Base case: reached the end
    if maze[x][y] == 'E':
        path.append((x, y))
        return True
    # Mark current cell as visited
    maze[x][y] = '#'
    # Possible moves: right, down, left, up
    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] in (' ', 'E'):
            if solve_maze(maze, nx, ny, path):
                path.append((x, y))
                return True
    return False

# Example usage:
maze = [
    ['S', ' ', ' ', '#', ' ', ' ', ' '],
    ['#', '#', ' ', '#', ' ', '#', ' '],
    [' ', ' ', ' ', ' ', ' ', '#', ' '],
    [' ', '#', '#', '#', ' ', '#', ' '],
    [' ', ' ', ' ', '#', ' ', ' ', 'E']
]
path = []
solve_maze(maze, 0, 0, path)
print("Path to exit:", path[::-1])

# print(len(maze))
# print(maze[len(maze)-1][len(maze[4])-1])