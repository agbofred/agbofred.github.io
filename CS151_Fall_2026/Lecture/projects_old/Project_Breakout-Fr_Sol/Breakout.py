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
                brick.set_color("WHITE")
                brick.set_fill_color(col)
                brick.set_filled(True)
                gw.add(brick)
                gw.brick_count += 1  

        gw.lives = 3
    def draw_paddle():
        x = GWINDOW_WIDTH / 2 - PADDLE_WIDTH / 2
        y = (1 - BOTTOM_FRACTION) * GWINDOW_HEIGHT
        gw.paddle=GRect(x,y,PADDLE_WIDTH, PADDLE_HEIGHT)
        gw.paddle.set_fill_color("grey")
        gw.paddle.set_filled(True)
        gw.add(gw.paddle)
    # Paddle event that allows player to drag mouse while paddle moves along that direction
    def paddle_move(e):
        if e.get_x()>0 and e.get_x() + PADDLE_WIDTH < GWINDOW_WIDTH:
            gw.paddle.move(e.get_x()-gw.paddle.get_x(), 0)

    ## Draw a ball at the center of the window
    def create_ball():
        gw.ball = GOval(GWINDOW_WIDTH/2 - BALL_DIAMETER/2, GWINDOW_HEIGHT/2 - BALL_DIAMETER/2, BALL_DIAMETER,BALL_DIAMETER)
        gw.ball.set_filled(True)
        gw.add(gw.ball)

        
        gw.vy = INITIAL_Y_VELOCITY
        gw.vx= random.uniform(MIN_X_VELOCITY, MAX_X_VELOCITY)
        gw.ball_moving = False
        if random.uniform(0,1) < 0.5:
            gw.vx *= -1 

    # Call back function to uodate the valocity of ball movement upon clicking
    def update_ball():
            if gw.ball_moving:
                if gw.ball.get_x() + gw.vx < 0:
                    gw.vx *= -1
                elif gw.ball.get_x() + BALL_DIAMETER > GWINDOW_WIDTH:
                    gw.vx *= -1
                
                if gw.ball.get_y() + gw.vy < 0:
                    gw.vy *= -1
                elif gw.ball.get_y() + BALL_DIAMETER > GWINDOW_HEIGHT:
                    gw.ball_moving = False
                    gw.remove(gw.ball)
                    gw.lives -= 1
                    if gw.lives:
                        create_ball()
                gw.ball.move(gw.vx, gw.vy)
            
            check_collision()
            if gw.lives < 1 or gw.brick_count < 1:
                gw.close()


    # Event to set the state of the ball to moving or not moving
    def ball_movement(e):
        if not gw.ball_moving:
            gw.ball_moving = True
        else:
            gw.ball_moving = False
    
    ## Function to to retreive what the ball is colliding with
    def get_coliding_object():
        x = gw.ball.get_x()
        y = gw.ball.get_y()
        #below is a list containing tuple elements that store the 4 points where ball can colide with an object
        points=[(x,y),(x+BALL_DIAMETER, y), (x,y+BALL_DIAMETER), (x + BALL_DIAMETER, y + BALL_DIAMETER)]
        for point in points:
            d_obj = gw.get_element_at(*point)
            if d_obj:
                return d_obj
        return None

    # Checking the coliding object and updating accordingly
    def check_collision():
        collision = get_coliding_object()
        if collision:
            #check paddle:
            if collision == gw.paddle:
                if gw.vy > 0:
                    gw.vy *= -1
                dist = get_obj_center(gw.ball)[0] - get_obj_center(gw.paddle)[0]
                gw.vx = dist/8
            else:
                gw.vy *= -1
                gw.remove(collision)
                gw.brick_count -= 1
                gw.vy *= 1.05 # Adding one more force



    setup()
    draw_paddle()
    create_ball()
    gw.add_event_listener("mousemove", paddle_move)
    gw.add_event_listener("click", ball_movement)
    gw.set_interval(update_ball, 20)


    # Extra
    def get_obj_center(obj):
        x = obj.get_x() + obj.get_width()/2
        y = obj.get_y() + obj.get_height()/2
        return x,y

    
# Startup code
if __name__ == "__main__":
    breakout()
