######################################################################
# Name: Ethan Honeycutt
# Collaborators (if any): ChatGPT
# Section leader's name:
# List of extensions made (if any): 1
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
       
        ystart = GWINDOW_HEIGHT * TOP_FRACTION
        xstart = BRICK_SEP // 2
        color = ["Red", "Red", "Orange", "Orange", "Green", "Green", "Cyan", "Cyan", "Blue", "Blue"]
        bricks = []
        gw.bricks_count=0
        for row in range(N_ROWS):
            ro_col = row % len(color)
            b_col = (color[ro_col]).strip().upper()
            for col in range(N_COLS):
                x = xstart + col  * (BRICK_WIDTH + BRICK_SEP) + BRICK_SEP
                y = ystart + row  * (BRICK_HEIGHT + BRICK_SEP) + BRICK_SEP
                brick = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
                brick.set_fill_color(b_col)
                brick.set_color("white")
                brick.set_filled(True)
                gw.add(brick)
                #bricks.append(brick)
                gw.bricks_count+=1
        gw.lives=3

    # Function to create the paddle
    def create_paddle():
        gw.paddle = GRect((GWINDOW_WIDTH - PADDLE_WIDTH) / 2, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)
        gw.paddle.set_filled(True)
        #gw.paddle.fill_color = ("black")
        gw.add(gw.paddle)
        #return paddle


    # Function to create the ball
    def create_ball():
        x = (GWINDOW_WIDTH - BALL_DIAMETER) / 2
        y = (GWINDOW_HEIGHT - BALL_DIAMETER) / 2
        gw.ball = GOval(x, y, BALL_DIAMETER, BALL_DIAMETER)
        gw.ball.set_filled(True)
        gw.add(gw.ball)

        # Set initial ball velocities (random)
        gw.x_velocity = random.uniform(MIN_X_VELOCITY, MAX_X_VELOCITY)
        gw.y_velocity = INITIAL_Y_VELOCITY
        gw.ball_movement = False
        if random.uniform (0, 1) < 0.5:
            gw.x_velocity *= -1
        # return ball


    # Function to move the ball
    def move_ball(e):
        if not gw.ball_movement: 
            gw.ball_movement = True
        else:
            gw.ball_movement = False
        # ball.move(ball.x_velocity, ball.y_velocity)

        # Check for collision with the walls
        # if ball.x <= 0 or ball.x + BALL_DIAMETER >= GWINDOW_WIDTH:
        #     ball.x_velocity = -ball.x_velocity

        # if ball.y <= 0:
        #     ball.y_velocity = -ball.y_velocity

        # if ball.y >= GWINDOW_HEIGHT:
        #     # Ball lost, handle life count or game over
        #     print("Ball lost!")

        # Handle paddle movement
        
        
    def move_paddle(e):
        if e.get_x() > 0 and e.get_x() + PADDLE_WIDTH < GWINDOW_WIDTH:
            gw.paddle.move(e.get_x() - gw.paddle.get_x(), 0)

    def update_ball_position():
        if gw.ball_movement:
            if gw.ball.get_x() + gw.x_velocity < 0:
                gw.x_velocity *= -1
            elif gw.ball.get_x() + BALL_DIAMETER > GWINDOW_WIDTH:
                gw.x_velocity *= -1
            
            if gw.ball.get_y() + gw.y_velocity < 0:
                gw.y_velocity *= -1
            elif gw.ball.get_y() + BALL_DIAMETER > GWINDOW_HEIGHT:
                gw.ball_movement = False
                gw.remove(gw.ball)
                gw.lives -= 1
                if gw.lives:
                    create_ball()
            gw.ball.move(gw.x_velocity, gw.y_velocity)
            
            check_collision()
            if gw.lives < 1 or gw.bricks_count < 1:
                gw.close()
       
        #############################
        # if gw.ball_movement:
        #     if gw.ball.get_x() + gw.x_velocity < 0:
        #         gw.x_velocity *= -1
        #     elif gw.ball.get_x() + BALL_DIAMETER > GWINDOW_WIDTH:
        #         gw.x_velocity *= 1

        #     if gw.ball.get_y() + gw.y_velocity < 0:
        #         gw.y_velocity *= -1
        #     elif gw.ball.get_y() + BALL_DIAMETER > GWINDOW_WIDTH:
        #         gw.ball_movement = False
        #     gw.ball.move(gw.x_velocity, gw.y_velocity)
        #     #print(gw.x_velocity, gw.y_velocity)
        #     gw.ball.move(gw.x_velocity, gw.y_velocity)
        
        ###########################


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
                if gw.x_velocity > 0:
                    gw.y_velocity *= -1
                dist = get_obj_center(gw.ball)[0] - get_obj_center(gw.paddle)[0]
                gw.x_velocity = dist/8
            else:
                gw.y_velocity *= -1
                gw.remove(collision)
                gw.bricks_count -= 1
                gw.y_velocity *= 1.05 # Adding one more force
                
                
    def get_obj_center(obj):
        x = obj.get_x() + obj.get_width()/2
        y = obj.get_y() + obj.get_height()/2
        return x,y


    setup()
    create_paddle()
    create_ball()
    gw.add_event_listener("click", move_ball)
    gw.set_interval(update_ball_position, 10) 
    gw.add_event_listener("mousemove", move_paddle)

# Startup code
if __name__ == "__main__":
    breakout()
