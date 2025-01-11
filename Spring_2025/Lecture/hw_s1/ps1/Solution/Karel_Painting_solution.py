#====================================================
# Filename: Karel_Painting.py
# 
# Your name:ccxc
# Who did you work with (if anyone)?:
# Estimate for time spent on this prob (in hrs)?:
#====================================================

# I've just laid out a basic starting function below, but remember that you
# absolutely should define more helping functions to decompose the problem
# into smaller pieces! Here I'm leaving those pieces (and helper functions)
# up to you to design and name as you see fit. Don't forget comments!

import karel

def main():
    """ Function to cause Karel to paint 3 sides of its house and then go indoors. """
    # You can add your code below
    #move()
    if facing_east():
        turn_around()
    if facing_north():
        turn_left()
    if facing_south():
        turn_right()
    for i in range(3):
        while left_is_blocked():
            put_beeper()
            move()
        turn_left()
        move()
    while left_is_blocked():
        move()
    turn_left()
    move()
    
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
