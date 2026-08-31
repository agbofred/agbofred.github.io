
import karel

def dewinter():
    """ Add leaves to the tops of the trees. """
    while beepers_in_bag():
        travel_to_tree()
        move_up_tree()
        add_leaves()
        move_down_tree()
    move_to_obstacle()


def travel_to_tree():
    """ Moves to the base of the next tree. """
    move_to_obstacle()

def move_up_tree():
    """ Scales a tree until it reaches the top. """
    turn_left()
    while right_is_blocked():
        if front_is_clear():
            move()

def add_leaves():
    """ Add the square of leaves to the top. """
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()

def move_to_obstacle():
    while front_is_clear():
        move()

def move_down_tree():
    move_to_obstacle()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
