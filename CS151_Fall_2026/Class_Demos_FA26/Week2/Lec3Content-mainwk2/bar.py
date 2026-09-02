import karel

def main():
    """This is where the main program runs"""
    a_bar_per_time()

def a_bar_per_time():
    "Create the bar chat per street" 
    if front_is_clear():
        while beepers_present():
            paint()

def paint():
    """Create the bars in practice"""
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
        move()
        
def up():
    while beepers_present():
        move()
    put_beeper()

def down():
    turn_around()
    while front_is_clear():
        move()
    
def turn_right():
    for i in range(3):
        turn_left()
        
def turn_around():
    for i in range(2):
        turn_left()
    
   