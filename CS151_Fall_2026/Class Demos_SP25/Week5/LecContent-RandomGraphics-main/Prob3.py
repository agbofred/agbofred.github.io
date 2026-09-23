"""
Tracing out a drunken robot walk
"""

from pgl import GWindow, GRect, GOval
import random


WIDTH = 800
HEIGHT = 800
SIZE = 25
STEP = SIZE

gw = GWindow(WIDTH, HEIGHT)
# Center my coordinates 
x_robot = WIDTH/2
y_robot = HEIGHT/2
start = GRect(x_robot, y_robot, SIZE, SIZE)

start.set_filled(True)
start.set_fill_color("grey")
gw.add(start)

for i in range(50):
    dir = random.choice("NSWE")
    if dir =="N":
        y_robot -= STEP
    elif dir == "S":
        y_robot += STEP
    elif dir == "W":
        x_robot -= STEP
    else:
        x_robot += STEP

    new_start = GRect(x_robot, y_robot, SIZE, SIZE)

    new_start.set_filled(True)
    new_start.set_fill_color("grey")
    gw.add(new_start)


