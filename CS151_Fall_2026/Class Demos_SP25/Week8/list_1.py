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
BRICK_WIDTH = (GWINDOW_WIDTH - (N_COLS + 1) * BRICK_SEP) / N_COLS
BRICK_HEIGHT = BRICK_WIDTH / BRICK_ASPECT_RATIO

def bricks():
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    brick_count = 0
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
    for r in range(10):
            #rem = r % len(col_seq)
            #col = col_seq[rem]
            for c in range(10):
                x = 1 + c * (BRICK_WIDTH + BRICK_SEP)
                y = 1 + r * (BRICK_HEIGHT + BRICK_SEP)
                # NOTE: Rects drawn with origin upper left
                brick = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
                brick.set_color("WHITE")
                brick.set_fill_color(col_seq[r])
                brick.set_filled(True)
                gw.add(brick)
                print(brick_count)
                brick_count += 1  
                
if __name__ == "__main__":
    bricks()