######################################################################
# Name: Bryce Schrader
# Collaborators (if any): Farley Dugan
# Section leader's name: Ryan Strobel
# List of extensions made (if any):
######################################################################

"""
This program (once you have finished it) implements the Breakout game
"""

from pgl import GWindow, GRect, GOval
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

# Function to create bricks with specified color arrangement

    
# Function: breakout
def breakout():
    """The main program for the Breakout game."""
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    
    def create_bricks(gw):
        bricks = []
        color_sequence = ["Red", "Orange", "Green", "Cyan", "Blue"]
        
        for row in range(N_ROWS):
            color = color_sequence[row // 2 % len(color_sequence)]  # Alternate colors every two rows
            for col in range(N_COLS):
                x = BRICK_SEP * (col + 1) + col * BRICK_WIDTH
                y = TOP_FRACTION * GWINDOW_HEIGHT + BRICK_SEP * (row + 1) + row * BRICK_HEIGHT
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.set_filled(True)
                brick.set_color(color)
                print(color)
                gw.add(brick, x, y)
                bricks.append(brick)
        
        return bricks

    # Function to create and return the paddle
    def create_paddle():
        gw.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        gw.paddle.set_filled(True)
        paddle_x = (GWINDOW_WIDTH - PADDLE_WIDTH) / 2
        gw.add(gw.paddle, paddle_x, PADDLE_Y)

    # Function to update the paddle position based on mouse movement
    #def update_paddle_position(paddle, mouse_x):
    #    paddle_x = mouse_x - PADDLE_WIDTH / 2  # Adjust paddle position based on mouse x-coordinate
        # Ensure paddle does not move off the edges of the window
    #    if paddle_x < 0:
    #        paddle_x = 0
    #    elif paddle_x + PADDLE_WIDTH > GWINDOW_WIDTH:
    #        paddle_x = GWINDOW_WIDTH - PADDLE_WIDTH
    #    paddle.set_location(paddle_x, PADDLE_Y)
        




    # Create bricks
    bricks = create_bricks(gw)
    
    # Create the paddle
    

    def mouse_moved(e):
        #x = e.getX() - PADDLE_WIDTH / 2
        #x = max(0, min(x, GWINDOW_WIDTH - PADDLE_WIDTH))
        if e.get_x()> 0 and e.get_x() + PADDLE_WIDTH < GWINDOW_WIDTH:
            gw.paddle.move(e.get_x()- gw.paddle.get_x(),0)

    # Main event loop to track mouse movement
    create_paddle()
    gw.add_event_listener("mousemove", mouse_moved)

# Call the main function
if __name__ == "__main__":
    breakout()