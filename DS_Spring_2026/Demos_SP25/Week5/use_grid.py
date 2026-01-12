from grid import Grid

grid = Grid(4, 5, 0)
# Go through rows
for row in range(grid.getHeight()):
# Go through columns
    for column in range(grid.getWidth()):
        grid[row][column] = int(str(row) + str(column))
        print(grid)