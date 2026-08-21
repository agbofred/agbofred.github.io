########################################
# Name:
# Collaborators:
# Estimate time spent (hrs):
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():

    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        print("You clicked the window!") # Delete this once you start Part C
        if sq.contains(event.get_x(), event.get_y()):
            x_new = random.randint(0, GW_WIDTH-SQUARE_SIZE)
            y_new = random.randint(0, GW_HEIGHT-SQUARE_SIZE)
            sq.set_location(x_new, y_new)
            sq.set_fill_color(Randomcolor())
            score = int(label.get_label())
            label.set_label(f'{score+1}')
        else:
            label.set_label(f'{0}')

    

        


    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function
    sq = GRect(GW_WIDTH/2 - SQUARE_SIZE-2, GW_HEIGHT/2-SQUARE_SIZE/2, SQUARE_SIZE, SQUARE_SIZE)
    sq.set_fill_color(Randomcolor())
    sq.set_filled(True)
    
    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    label = GLabel("0")
    label.set_font(SCORE_FONT)
    gw.add(sq)
    gw.add(label, SCORE_DX, GW_HEIGHT-SCORE_DX)
    gw.add_event_listener("click", on_mouse_down)

def Randomcolor():
    c="#"
    for i in range(6):
        c += random.choice("123456789ABCDEF")
    return c




if __name__ == '__main__':
    clicky_box()
