import karel


def main():
    while front_is_clear():
        plot_bar()

# def count_beeper():
#     while beepers_present():
#            c = c + 1
    
def plot_bar():
    while beepers_present():
        pick_beeper()
        c = c + 1
    turn_right()
    for i in range(c-1):
        put_beeper()
        move()
    turn_around()
    for i in range(c):
            move()
    turn_right()
    move()
    
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
        