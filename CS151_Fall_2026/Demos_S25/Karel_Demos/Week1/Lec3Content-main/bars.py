import karel


def main():
    if front_is_clear():
        a_bar_per_time()


def a_bar_per_time():
    if front_is_clear():
        while beepers_present():
            paint()

def paint():
    if beepers_present():
        pick_beeper()
        checker()
    else:
        put_beeper()

def checker():
    if beepers_present():
        turn_right()
        up()
        down()
        turn_right()
    else:
        put_beeper()
        # if front_is_clear():
        move()

def up():
    while beepers_present():
        move()
    put_beeper()
            
def down():
    turn_around()
    while front_is_clear():
        move()
    
    
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
        