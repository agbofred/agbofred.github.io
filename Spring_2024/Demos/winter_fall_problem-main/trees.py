import karel
def main():
    """ Here is our general solution with higher level of decomposition"""
    for i in range(3):
        find_next_tree()
        remove_leaves()

def find_next_tree():
    """ the codes to find next tree"""
    while front_is_clear():
        move()

def remove_leaves():
    """ codes to remove leaves"""
    move_up()
    deleaf()
    move_down()

def move_up():
    """Codes for moving Karel up the tree"""
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
    """Moving Karel to down the tree to find the next tree"""
    while front_is_clear():
        move()
    turn_left()

def turn_right(): # Function to turn karel to the right
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()
        