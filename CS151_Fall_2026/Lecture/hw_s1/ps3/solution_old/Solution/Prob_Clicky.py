from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500      # Width of window
GW_HEIGHT = 500     # Height of window
SQUARE_SIZE = 50    # Width and height of square
SCORE_DY = 10       # Distance up from bottom of window to baseline
SCORE_DX = 10       # Distance from left of window to origin
SCORE_FONT = "bold 40pt 'serif'"

def clicky_box():

    # Defining the callback function, which you won't need until Part C
    def on_mouse_click(event):
        print("You clicked the window!") # Delete this once you start Part C

        if sq.contains(event.get_x(), event.get_y()):
            newx = random.randint(0, GW_WIDTH - SQUARE_SIZE)
            newy = random.randint(0, GW_HEIGHT - SQUARE_SIZE)
            sq.set_location(newx, newy)
            sq.set_color(random_color())

            score = int(label.get_label())
            label.set_label(f"{score+1}")
        else:
            label.set_label(f"{0}")



    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function

    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    sq = GRect(GW_WIDTH / 2 - SQUARE_SIZE / 2, GW_HEIGHT / 2 - SQUARE_SIZE / 2,
               SQUARE_SIZE, SQUARE_SIZE)
    sq.set_filled(True)
    sq.set_color(random_color())

    label = GLabel("0")
    label.set_font(SCORE_FONT)


    gw.add(sq)
    gw.add(label, SCORE_DX, GW_HEIGHT - SCORE_DY)

    gw.add_event_listener("mousedown", on_mouse_click)


def random_color():
    col = "#"
    for _ in range(6):
        col += random.choice("0123456789ABCDEF")
    return col










if __name__ == '__main__':
    clicky_box()
