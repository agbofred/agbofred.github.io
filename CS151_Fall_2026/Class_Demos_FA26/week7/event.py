from pgl import GWindow, GOval, GRect
from pgl_tools import create_filled_circ
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
        bg.set_fill_color('grey')
        
circ = create_filled_circ(WIDTH/2, HEIGHT/2, 50, color="white")
def move_diag(e):
    dx = e.get_x()
    dy = e.get_y()
    circ.move(dx,dy)
    
def move_across():
    if circ.get_x() == 200:
        timer.stop()
    circ.move(1,1)

gw = GWindow(WIDTH, HEIGHT)
bg = GRect(0, 0, WIDTH, HEIGHT)
bg.set_filled(True)
gw.add(bg)
gw.add(circ)

gw.add_event_listener("click", back_ground)
gw.add_event_listener('dblclick', move_diag)
timer = gw.set_interval(move_across, 20)
