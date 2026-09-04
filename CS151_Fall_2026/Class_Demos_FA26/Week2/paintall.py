import karel

def main():
    """ Run the painting """
    while no_beepers_present():
        put_beeper()
        wonder()
        if beepers_present():
            reset()
        
def wonder():
    if front_is_blocked():
        turn_left()
    move()
    
def reset():
    """ reset karel to a new sqaure world"""
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    
def turn_right():
    for i in range(3):
        turn_left()
