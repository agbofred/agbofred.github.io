"""
File: maze.py
Project 7.9

Determine the solution to a maze problem.
Uses a gid to represent the maze.  This grid is input from
a text file.  Uses a stack-based backtracking algorithm.
"""

from grid import Grid
from arraystack import ArrayStack

def main():
    maze = getMazeFromFile()
    print(maze)
    (startRow, startCol) = findStartPos(maze)
    success = getOut(startRow, startCol, maze)
    if success:
        print("Maze solved:")
        print(maze)
    else:
        print("No path out of this maze")
    
def getMazeFromFile():
    """Reads the maze from a text file and returns a grid that
    represents it."""
    

def findStartPos(maze):
    """Returns the position of the start symbol in the grid."""
   
                
def getOut(row, column, maze):
    """(row,column) is the position of the start symbol in the maze.
    Returns True if the maze can be solved or False otherwise."""
    # States are tuples of coordinates of cells in the grid.
   
            # Cell has not been visited, so mark it and push adjacent unvisited
            # positions onto the stack
            
            # Try NORTH
                        
            # Try SOUTH
                         
            # Try EAST
                         
            # Try WEST
            

if __name__ == "__main__": main()
