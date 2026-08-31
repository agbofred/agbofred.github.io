
import karel

def make_checkerboard():
    """
    Function to draw a checkerboard pattern using beepers
    on any rectangular grid.
    """
    put_beeper()
    if front_is_blocked(): # to handle 1xX grids
        turn_left()
    while front_is_clear():
        draw_row()
        handle_corner()

def turn_right():
    """ Turns Karel to the right. """
    turn_left()
    turn_left()
    turn_left()


def draw_row():
    """
    Draws a single row with alternating beepers.
    """
    while front_is_clear():
        draw_pair()

def handle_corner():
    """
    Handles turning around at edges for next pass.
    """
    if facing_east():
        turn_left()
        if front_is_clear():
            draw_pair()
            turn_left()
    else:
        turn_right()
        if front_is_clear():
            draw_pair()
            turn_right()

def draw_pair():
    """
    Moves and drops alternating beepers and empty spaces.
    """
    if beepers_present():
        if front_is_clear():
            move()
    else:
        if front_is_clear():
            move()
            put_beeper()


