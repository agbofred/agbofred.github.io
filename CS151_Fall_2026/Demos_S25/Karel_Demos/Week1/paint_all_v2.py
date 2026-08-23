
import karel

def main():
    while no_beepers_present():
        put_beeper()
        wonder()
        if beepers_present():
            reset()

def wonder():
    if front_is_blocked():
        turn_left()
    move()
        
def turn_right():
    for i in range(3):
        turn_left()
        
def reset():
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    