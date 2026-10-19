from MazeUtils import is_path_to_freedom, twisty_maze_for

GROUPNAME = "YourNamesHere"
ESCAPE_PATH = "SEES"

def twisty(path_out):
    """Generates a twisty maze unique to the NAME and checks the provided path
    to see if it successfully escapes the maze.

    Args:
        path_out (str): The sequence of N,S,E, and W directions to follow
    """
    start = twisty_maze_for(GROUPNAME)
    print(f"Starting room id is: {hex(id(start))}")

    if is_path_to_freedom(start, path_out): # PLACE BREAKPOINT ON THIS LINE
        print("Congratulations! You've found your way out of your twisty labyrinth.")
    else:
        print("Sorry, but you're still stuck in your twisty labyrinth.")


if __name__ == '__main__':
    twisty(ESCAPE_PATH)
