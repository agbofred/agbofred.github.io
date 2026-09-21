# File: Breakout.py
# By Jed

"""
This program (once you have finished it) implements the Breakout game
"""

from pgl import GWindow, GOval, GRect, GState
import random

# Constants
GWINDOW_WIDTH = 360
GWINDOW_HEIGHT = 600
N_ROWS = 10
N_COLS = 10
BRICK_ASPECT_RATIO = 4 / 1
BRICK_TO_BALL_RATIO = (
    3 / 1
)  # This was originally 3 / 2 but 3 / 1 seems more appropriate?
BRICK_TO_PADDLE_RATIO = 2 / 3
BRICK_SEP = 2
TOP_FRACTION = 0.1
BOTTOM_FRACTION = 0.05
N_BALLS = 3
TIME_STEP = 10
INITIAL_Y_VELOCITY = 3.0
MIN_X_VELOCITY = 1.0
MAX_X_VELOCITY = 3.0

# Derived Constants
BRICK_WIDTH = (GWINDOW_WIDTH - (N_COLS + 1) * BRICK_SEP) / N_COLS
BRICK_HEIGHT = BRICK_WIDTH / BRICK_ASPECT_RATIO
PADDLE_WIDTH = BRICK_WIDTH / BRICK_TO_PADDLE_RATIO
PADDLE_HEIGHT = BRICK_HEIGHT / BRICK_TO_PADDLE_RATIO
PADDLE_Y = (1 - BOTTOM_FRACTION) * GWINDOW_HEIGHT - PADDLE_HEIGHT
BALL_SIZE = BRICK_WIDTH / BRICK_TO_BALL_RATIO

# Function: breakout


def breakout():
    """The main program for the Breakout game."""

    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    gs = GState()

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
        gs.brick_count = 0
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
                gs.brick_count += 1

        gs.lives = 3

    def draw_paddle():
        """
        Draws the paddle to the screen.
        """
        x = GWINDOW_WIDTH / 2 - PADDLE_WIDTH / 2
        y = (1 - BOTTOM_FRACTION) * GWINDOW_HEIGHT
        gs.paddle = GRect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        gs.paddle.set_fill_color("Gray")
        gs.paddle.set_filled(True)
        gw.add(gs.paddle)

    def update_paddle(event):
        """
        Called on mouse drag to move paddle horizontal location to
        current mouse location (with window bounds).
        """
        # NOTE: movement of an object is relative to current position, not absolute
        if event.get_x() > 0 and event.get_x() + PADDLE_WIDTH < GWINDOW_WIDTH:
            gs.paddle.move(event.get_x() - gs.paddle.get_x(), 0)

    def draw_ball():
        """
        Draws the ball and sets up initial ball velocities
        """
        x = GWINDOW_WIDTH / 2 - BALL_SIZE / 2
        y = GWINDOW_HEIGHT / 2 - BALL_SIZE / 2
        gs.ball = GOval(x, y, BALL_SIZE, BALL_SIZE)
        gs.ball.set_fill_color("black")
        gs.ball.set_filled(True)
        gw.add(gs.ball)

        gs.ball_moving = False
        gs.vy = INITIAL_Y_VELOCITY
        gs.vx = random.uniform(MIN_X_VELOCITY, MAX_X_VELOCITY)
        if random.uniform(0, 1) < 0.5:
            gs.vx *= -1

    def update_ball():
        """
        Called on a schedule to animate the motion of the ball
        and check for potential collisions or win conditions.
        """
        if gs.ball_moving:
            if gs.ball.get_x() + gs.vx < 0:
                gs.vx *= -1
            elif gs.ball.get_x() + BALL_SIZE > GWINDOW_WIDTH:
                gs.vx *= -1

            if gs.ball.get_y() + gs.vy < 0:
                gs.vy *= -1
            elif gs.ball.get_y() + BALL_SIZE > GWINDOW_HEIGHT:
                gs.ball_moving = False
                gw.remove(gs.ball)
                gs.lives -= 1
                if gs.lives:
                    draw_ball()
            gs.ball.move(gs.vx, gs.vy)

            check_and_update_collisions()

            if gs.lives < 1 or gs.brick_count < 1:
                gw.close()

    def start_movement(event):
        """
        Callback function to start ball movement upon click.
        """
        if not gs.ball_moving:
            gs.ball_moving = True
        else:
            gs.ball_moving = False

    def get_colliding_object():
        """
        Retrieves any object the ball is currently colliding
        with by checking the 4 corners of the ball.
        """
        x = gs.ball.get_x()
        y = gs.ball.get_y()
        pts = [
            (x, y),
            (x + BALL_SIZE, y),
            (x, y + BALL_SIZE),
            (x + BALL_SIZE, y + BALL_SIZE),
        ]
        for pt in pts:
            obj = gw.get_element_at(*pt)
            if obj:
                return obj
        return None

    def check_and_update_collisions():
        """
        Handles potential collision updates with
        paddle or blocks.
        """
        collision = get_colliding_object()
        if collision:
            # Check paddle:
            if collision == gs.paddle:
                if gs.vy > 0:
                    gs.vy *= -1
                dist = get_obj_center(gs.ball)[0] - get_obj_center(gs.paddle)[0]
                gs.vx = dist/8
            else:
                gs.vy *= -1
                gw.remove(collision)
                gs.brick_count -= 1
                gs.vy *= 1.05  # Adding a "kicker"

    setup()
    draw_paddle()
    draw_ball()
    gw.add_event_listener("mousemove", update_paddle)
    gw.add_event_listener("click", start_movement)
    timer = gw.set_interval(update_ball, 20)

    # Extra
    def get_obj_center(obj):
        x = obj.get_x() + obj.get_width()/2
        y = obj.get_y() + obj.get_height()/2
        return x,y

# Startup code

if __name__ == "__main__":
    breakout()
