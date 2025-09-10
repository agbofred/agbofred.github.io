def solvemaze(maze, x,y, path):
    # Define the base case: When it reaches an end
    if maze[x][y] == "E":
        path.append((x,y))
        return True
    
    # Mark current cell as visited
    maze[x][y] = '#'
    
    #What are the possible moves
            # right, down,  up,     left
    moves = [(0,1), (1,0), (-1,0), (0,-1)]
    for dx, dy in moves:
        nx, ny = x + dx, y+ dy
        #if movement is within the rows and also within the column and either at  empty or exit "E" 
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] in (' ','E'):
            if solvemaze(maze, nx, ny, path):
                path.append((x,y))
                return True
    return False

            
    
    
    
    
    
maze=[
    ['S', ' ', '#'],
    ['E', '#', 'E']
]
# maze2= [
#     ['S', ' ', ' ', '#', ' ', ' ', ' '],
#     ['#', '#', ' ', '#', ' ', '#', ' '],
#     [' ', ' ', ' ', ' ', ' ', '#', ' '],
#     [' ', '#', '#', '#', ' ', '#', ' '],
#     [' ', ' ', ' ', '#', ' ', ' ', 'E']
# ]
path =[]
solvemaze(maze, 0,0,path)
print("Paths:", path[::-1])

