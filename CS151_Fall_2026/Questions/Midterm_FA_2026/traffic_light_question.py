"""
Traffic Light (Graphics and Callbacks)

The starter code below draws a traffic light on a black background.
All three lights start unlit (dark gray), except the red light, which
starts lit. Your job is to make the light change after 1 second.

Complete the three functions marked  ### YOUR CODE HERE ###.
Do NOT change any other code.

Part (a)  turn_on_light(light, color)
    Takes a GOval and a color string, and sets the light to that color.

Part (b)  turn_off_light(light)
    Takes a GOval and sets it back to the unlit color, UNLIT_COLOR.

Part (c)  change_light()
    This is the callback function. It takes no parameters and is called
    once, 1 second after the program starts. When it runs, it must:
        1. turn OFF the red light, and
        2. turn ON the green light using GREEN.
    You must use the functions you wrote in parts (a) and (b).

Hint: the last line of the starter code schedules change_light with
gw.set_timeout(function, delay_in_milliseconds). Pass the function
itself (no parentheses).
"""

from pgl import GWindow, GRect, GOval

WIDTH = 400
HEIGHT = WIDTH * 2.5
LIGHT_SIZE = WIDTH * 0.4
UNLIT_COLOR = "#333333"
RED = "#C51F1F"
YELLOW = "#E6C21A"
GREEN = "#1FA83A"


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


### PART (a) ###
def turn_on_light(light, color):
    """Sets the given light to the given color.

    Inputs:
        light (GOval): the light to turn on
        color (str): the color to give the light
    """
    ### YOUR CODE HERE ###
    light.set_color(color)

### PART (b) ###
def turn_off_light(light):
    """Sets the given light back to UNLIT_COLOR.

    Inputs:
        light (GOval): the light to turn off
    """
    ### YOUR CODE HERE ###
    light.set_color(UNLIT_COLOR)

### PART (c) ###
def change_light():
    """Callback: turns off the red light and turns on the green light."""
    ### YOUR CODE HERE ###
    turn_off_light(gw.red_light)
    turn_on_light(gw.yellow_light, YELLOW)
    turn_on_light(gw.green_light, GREEN)


gw = GWindow(WIDTH, HEIGHT)
paint_it_black()

gw.red_light = create_light(WIDTH / 2, 0.5 * WIDTH)
gw.yellow_light = create_light(WIDTH / 2, 1.0 * WIDTH)
gw.green_light = create_light(WIDTH / 2, 1.5 * WIDTH)

gw.red_light.set_color(RED)

gw.add(gw.red_light)
gw.add(gw.yellow_light)
gw.add(gw.green_light)

timer = gw.set_timeout(change_light, 1000)
timer = gw.set_timeout(change_light, 2000)
timer = gw.set_timeout(change_light, 3000)
