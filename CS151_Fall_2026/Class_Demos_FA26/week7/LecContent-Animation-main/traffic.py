from pgl import GWindow, GRect, GOval

WIDTH = 400
HEIGHT = WIDTH * 3
LIGHT_SIZE = WIDTH * 0.8
UNLIT_COLOR = "#333333"


def paint_it_black():
    """Adds a black background to the scene."""
    bg = GRect(0, 0, WIDTH, HEIGHT)
    bg.set_filled(True)
    gw.add(bg)


def create_light(x_cent, y_cent):
    """Creates a single light at a position on a stoplight

    Inputs:
        x_cent (int/float): the horizontal center position of the light
        y_cent (int/float): the vertical center position of the light
    Outputs:
        (GOval): the circle representing the light
    """
    light = GOval(
        x_cent - LIGHT_SIZE / 2, y_cent - LIGHT_SIZE / 2, LIGHT_SIZE, LIGHT_SIZE
    )
    light.set_filled(True)
    light.set_color(UNLIT_COLOR)
    return light


gw = GWindow(WIDTH, HEIGHT)
paint_it_black()

red_light = create_light(WIDTH / 2, 0.5 * WIDTH)
yellow_light = create_light(WIDTH / 2, 1.5 * WIDTH)
green_light = create_light(WIDTH / 2, 2.5 * WIDTH)

gw.add(red_light)
gw.add(yellow_light)
gw.add(green_light)
