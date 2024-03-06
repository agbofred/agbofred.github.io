######################################################################
# Name:By Fred
# Collaborators (if any):
# Section leader's name:
# List of extensions made (if any):
######################################################################

"""
This program (once you have finished it) implements the Breakout game
"""

from pgl import GWindow, GOval, GRect
import random

# Constants
GWINDOW_WIDTH = 360                     # Width of the graphics window
GWINDOW_HEIGHT = 600                    # Height of the graphics window
N_ROWS = 10                             # Number of brick rows
N_COLS = 10                             # Number of brick columns
BRICK_ASPECT_RATIO = 4 / 1              # Width to height ratio of a brick
BRICK_TO_BALL_RATIO = 3 / 1             # Ratio of brick width to ball size
BRICK_TO_PADDLE_RATIO = 2 / 3           # Ratio of brick to paddle width
BRICK_SEP = 2                           # Separation between bricks (in pixels)
TOP_FRACTION = 0.1                      # Fraction of window above bricks
BOTTOM_FRACTION = 0.05                  # Fraction of window below paddle
N_BALLS = 3                             # Number of balls (lives) in a game
TIME_STEP = 10                          # Time step in milliseconds
INITIAL_Y_VELOCITY = 3.0                # Starting y velocity downwards
MIN_X_VELOCITY = 1.0                    # Minimum random x velocity
MAX_X_VELOCITY = 3.0                    # Maximum random x velocity

# Derived Constants
BRICK_WIDTH = (GWINDOW_WIDTH - (N_COLS + 1) * BRICK_SEP) / N_COLS
BRICK_HEIGHT = BRICK_WIDTH / BRICK_ASPECT_RATIO
PADDLE_WIDTH = BRICK_WIDTH / BRICK_TO_PADDLE_RATIO
PADDLE_HEIGHT = BRICK_HEIGHT / BRICK_TO_PADDLE_RATIO
PADDLE_Y = (1 - BOTTOM_FRACTION) * GWINDOW_HEIGHT - PADDLE_HEIGHT
BALL_DIAMETER = BRICK_WIDTH / BRICK_TO_BALL_RATIO


# Function: breakout
def breakout():
    """The main program for the Breakout game."""

    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)

    # You fill in the rest of this function along with any additional
    # helper and callback functions you need

    def setup():
        """
        Draws initial blocks to the screen and sets
        overall game parameters like the number of lives
        or the number of bricks on the screen.
        """
        ystart = GWINDOW_HEIGHT * TOP_FRACTION
        xstart = BRICK_SEP // 2
        col_seq = [
            "Red",
            "Red",
            "Orange",
            "Orange",
            "Green",
            "Green",
            "Cyan",
            "Cyan",
            "Blue",
            "Blue",
        ]
        gw.brick_count = 0
        for r in range(N_ROWS):
            rem = r % len(col_seq)
            col = col_seq[rem]
            for c in range(N_COLS):
                x = xstart + c * (BRICK_WIDTH + BRICK_SEP)
                y = ystart + r * (BRICK_HEIGHT + BRICK_SEP)
                # NOTE: Rects drawn with origin upper left
                brick = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
                #brick.set_color("WHITE")
                brick.set_fill_color(col)
                brick.set_filled(True)
                gw.add(brick)
                gw.brick_count += 1  

        gw.lives = 3

    setup()

# Startup code
if __name__ == "__main__":
    breakout()
