from pgl import GWindow, GRect, GOval

WIDTH = 800  # width of window
HEIGHT = 400  # height of window
BOX_SIZE = 50  # width and height of box
DART_SIZE = BOX_SIZE / 2  # diameter of dart
DART_X = 267  # dart thrown horizontal position
DART_Y = HEIGHT / 2  # dart thrown vertical position
STEP_INTERVAL = 10  # ms


def throw_dart():
    """
    'Throws' a dart to a position on the window, drawing a circle at that position
    """
    oval = GOval(DART_X, DART_Y - DART_SIZE / 2, DART_SIZE, DART_SIZE)
    oval.set_filled(True)
    gw.add(oval)
def move_across():
    rect.move(2,0)

gw = GWindow(WIDTH, HEIGHT)
rect = GRect(0, HEIGHT / 2 - BOX_SIZE / 2, BOX_SIZE, BOX_SIZE)
rect.set_filled(True)
rect.set_color("red")
gw.add(rect)
gw.set_interval(move_across, 50)
