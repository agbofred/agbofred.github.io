import karel
def main():
    """ Here are our subproblem 1"""
    for i in range(3):
        find_next_tree()
        remove_leaves()

def find_next_tree():
    """ Write the codes to find next tree"""
    while front_is_clear():
        move()

def remove_leaves():
    """ codes to remove leaves"""
    move_up()
    deleaf()
    move_down()


def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()
        
def move_up():
    """Codes for moving Krel up the tree"""
    turn_left()
    while right_is_blocked():
        move()


def deleaf():
    """ picking up beepers"""
    pick_beeper()
    for i in range(3):
        move()
        pick_beeper()
        turn_right()
    turn_left()

def move_down():
    """..."""
    while front_is_clear():
        move()
    turn_left()