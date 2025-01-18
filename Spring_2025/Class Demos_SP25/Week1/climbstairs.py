import karel

def main():
  while front_is_blocked():
            if facing_east():
                turn_left()
            if front_is_clear():
                step_up()
def step_up(): 
    move()
    turn_right()
    move()
    put_beeper()
def turn_right():
     for i in range(3):
          turn_left()