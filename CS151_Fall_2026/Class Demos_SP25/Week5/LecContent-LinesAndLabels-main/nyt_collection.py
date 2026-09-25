from pgl import GWindow, GRect, GLabel
"""
Algorithm:
Make boxes with text in them
Make each box and add it to the window in a grid fachion

"""

def make_and_place_box(word, x, y):
    """
    Make a box with the desired word centered in it
    
    Algorithms:
    1. Make a box of a desired dimention 
    2. make a label and place it centered in the box
    3. add everything to the window
    
    """
    box = GRect(x,y,BOX_WIDTH, BOX_HEIGHT)
    label = GLabel(word.upper())
    label.set_font("bold 24pt sans-sarif")
    # label.set_font("bold 20pt sans-serif")
    new_x = x + BOX_WIDTH / 2 - label.get_width() / 2
    new_y = y + BOX_HEIGHT / 2 + label.get_ascent()/2
    gw.add(box)
    gw.add(label, new_x, new_y)

BOX_WIDTH = 200
BOX_HEIGHT = 100
BOX_STEP = 10

WIDTH= 4 * (BOX_WIDTH + BOX_STEP)
HEIGHT= 4 * (BOX_HEIGHT + BOX_STEP)

gw = GWindow(WIDTH, HEIGHT)

# ROW 1
make_and_place_box("wayney", BOX_STEP/2, BOX_STEP/2)
make_and_place_box("Parliament", BOX_STEP/2 + BOX_WIDTH + BOX_STEP, BOX_STEP/2)
make_and_place_box("Standard", BOX_STEP/2 + 2 * (BOX_WIDTH + BOX_STEP), BOX_STEP/2)
make_and_place_box("lesson", BOX_STEP/2 + 3 * (BOX_WIDTH + BOX_STEP), BOX_STEP/2)

# ROW 2
make_and_place_box("kent", BOX_STEP/2, BOX_STEP/2 + BOX_HEIGHT + BOX_STEP) 
make_and_place_box("sync", BOX_STEP/2 + BOX_WIDTH + BOX_STEP, BOX_STEP/2 + BOX_HEIGHT + BOX_STEP)
make_and_place_box("Sheer", BOX_STEP/2 + 2 * (BOX_WIDTH + BOX_STEP), BOX_STEP/2 + BOX_HEIGHT + BOX_STEP)
make_and_place_box("colors", BOX_STEP/2 + 3 * (BOX_WIDTH + BOX_STEP), BOX_STEP/2 + BOX_HEIGHT + BOX_STEP)

#row3

# ROW 2
make_and_place_box("Stark", BOX_STEP/2, BOX_STEP/2 + 2 * (BOX_HEIGHT + BOX_STEP)) 
make_and_place_box("camel", BOX_STEP/2 + BOX_WIDTH + BOX_STEP, BOX_STEP/2 + 2 * (BOX_HEIGHT + BOX_STEP))
make_and_place_box("Banner", BOX_STEP/2 + 2 * (BOX_WIDTH + BOX_STEP), BOX_STEP/2 + 2 * (BOX_HEIGHT + BOX_STEP))
make_and_place_box("utter", BOX_STEP/2 + 3 * (BOX_WIDTH + BOX_STEP), BOX_STEP/2 + 2 * (BOX_HEIGHT + BOX_STEP))

# ROW 4
make_and_place_box("reseed", BOX_STEP/2, BOX_STEP/2 + 3 * (BOX_HEIGHT + BOX_STEP)) 
make_and_place_box("pure", BOX_STEP/2 + BOX_WIDTH + BOX_STEP, BOX_STEP/2 + 3 * (BOX_HEIGHT + BOX_STEP))
make_and_place_box("flag", BOX_STEP/2 + 2 * (BOX_WIDTH + BOX_STEP), BOX_STEP/2 + 3 * (BOX_HEIGHT + BOX_STEP))
make_and_place_box("salem", BOX_STEP/2 + 3 * (BOX_WIDTH + BOX_STEP), BOX_STEP/2 + 3 * (BOX_HEIGHT + BOX_STEP))