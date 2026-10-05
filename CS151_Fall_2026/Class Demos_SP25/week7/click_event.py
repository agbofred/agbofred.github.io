from pgl import GWindow, GOval, GRect
import random

WIDTH = 500
HEIGHT = 500
def random_color():
    color = "#"
    for i in range(6):
        color += random.choice("0123456789ABCDEF")
    return color
def back_ground(e):
    if e.get_x() < HEIGHT/2:
        bg.set_filled(True)
        bg.set_fill_color(random_color())
    else:
        bg.set_filled(True)
        bg.set_fill_color('purple')
        



gw = GWindow(WIDTH, HEIGHT)
bg = GRect(0, 0, WIDTH, HEIGHT)
bg.set_filled(True)
gw.add(bg)

gw.add_event_listener("click", back_ground)
