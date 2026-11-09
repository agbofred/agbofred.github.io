x = "omen"
y = 5

def mystery(y, z="odor"):

    def enigma(y):
        return (y + len(x)) % len(z)

    def puzzle(z):
        return (z + x)[i::y]

    s = ""
    for i in range(2):
        s += puzzle(z)
        if i % 2 == 1:
            s += z[enigma(y)]
        y -= 1
    return s

print(mystery(z="clay", y=y-1))
print(8%4)

"""
Mystery ()          Puzzle          Enigma
                    co                          
                    lon                 3
colony
                    





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

## Trafic behavious functions
def turn_on_red():
    gw.red_light.set_color(RED) # turn red On
    gw.yellow_light.set_color(UNLIT_COLOR)   # turn red off
    gw.green_light.set_color(UNLIT_COLOR)   # turn red off

def turn_on_yellow():
    gw.red_light.set_color(UNLIT_COLOR)   # turn red off
    gw.yellow_light.set_color(YELLOW)     # turn yellow On
    gw.green_light.set_color(UNLIT_COLOR)   # turn red off

def turn_on_green():
    gw.red_light.set_color(UNLIT_COLOR)   # turn red off
    gw.yellow_light.set_color(UNLIT_COLOR) # turn Yellow off
    gw.green_light.set_color(GREEN) # turn green On

def trafic_light():
    gw.set_timeout(turn_on_red, 2000)
    gw.set_timeout(turn_on_yellow, 3000)
    gw.set_timeout(turn_on_green, 4000)

gw = GWindow(WIDTH, HEIGHT)
paint_it_black()

gw.red_light = create_light(WIDTH / 2, 0.5 * WIDTH)
gw.yellow_light = create_light(WIDTH / 2, 1.0 * WIDTH)
gw.green_light = create_light(WIDTH / 2, 1.5 * WIDTH)

gw.add(gw.red_light)
gw.add(gw.yellow_light)
gw.add(gw.green_light)

timer = gw.set_timeout(trafic_light, 10)
