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
    gw.oval = GOval(DART_X, DART_Y - DART_SIZE / 2, DART_SIZE, DART_SIZE)
    gw.oval.set_filled(True)
    gw.add(gw.oval)

def move_across():
    b_width = rect.get_width()
    b_height = rect.get_height()
    step_size = WIDTH / (5000 / STEP_INTERVAL)
    # if rect.get_x() <= WIDTH - BOX_SIZE:
    if b_width <= 100:
        rect.move(step_size,0)
        rect.set_size(b_width+step_size, b_height+step_size)
    rect.move(step_size,0)
    if gw.oval is not None:
        gw.oval.move(step_size, 0)
        # GRect(rect.get_x(), rect.get_y(), b_width+step_size, b_height+step_size)
    
    
gw = GWindow(WIDTH, HEIGHT)
rect = GRect(0, HEIGHT / 2 - BOX_SIZE / 2, BOX_SIZE, BOX_SIZE)
rect.set_filled(True)
rect.set_color("red")
gw.add(rect)

gw.oval = None

gw.set_interval(move_across, STEP_INTERVAL)
gw.set_timeout(throw_dart, WIDTH//2 + 750)
