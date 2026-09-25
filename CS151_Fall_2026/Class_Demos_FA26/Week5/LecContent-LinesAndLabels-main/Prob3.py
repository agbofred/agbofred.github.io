from pgl import GWindow, GRect, GOval, GLine, GLabel
import random

# Constants
WIDTH = 200
HEIGHT = 600
THERM_HEIGHT = 500
THERM_WIDTH = 20
BULB_SIZE = 50
MARKER_STEP = 50
TEMP_STEP = 10

# Derived constants
BASE = HEIGHT // 2 + THERM_HEIGHT // 2
MARKER_START_Y = BASE - BULB_SIZE

def create_basic_thermometer():
    """Creates and adds a background and basic thermometer to the window"""
    bg = GRect(WIDTH, HEIGHT)
    bg.set_filled(True)
    bg.set_color('cyan')
    gw.add(bg)

    therm_bg = GLine(
        WIDTH / 2,
        HEIGHT / 2 - THERM_HEIGHT / 2,
        WIDTH / 2,
        BASE
    )
    therm_bg.set_line_width(20)
    therm_bg.set_color('white')
    gw.add(therm_bg)

    therm_base = GOval(
        WIDTH / 2 - BULB_SIZE / 2,
        BASE - BULB_SIZE / 2,
        BULB_SIZE,
        BULB_SIZE
    )
    therm_base.set_filled(True)
    therm_base.set_color('red')
    gw.add(therm_base)

    gauge = GLine(
        WIDTH / 2,
        BASE,
        WIDTH / 2,
        BASE - random.randint(0, THERM_HEIGHT)
    )
    gauge.set_line_width(THERM_WIDTH)
    gauge.set_color('red')
    gw.add(gauge)


gw = GWindow(WIDTH, HEIGHT)
create_basic_thermometer()

