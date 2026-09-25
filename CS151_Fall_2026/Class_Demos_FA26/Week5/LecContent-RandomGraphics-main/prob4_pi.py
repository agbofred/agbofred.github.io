"""
Random Pi problem
"""

from pgl import GWindow, GRect, GOval
import random
import math

WIDTH = 800
HEIGHT = 800
SIZE = 700
DART_SIZE = 20

gw = GWindow(WIDTH, HEIGHT)

background = GRect(WIDTH/2 - SIZE/2, HEIGHT/2 - SIZE/2, SIZE, SIZE)
background.set_fill_color("grey")
background.set_filled(True)
gw.add(background)

target_area = GOval(WIDTH/2 - SIZE/2, HEIGHT/2 - SIZE/2, SIZE, SIZE)
target_area.set_fill_color("darkgrey")
target_area.set_filled(True)
gw.add(target_area)

num_of_attempts = 500000
successful_strike = 0
for i in range(num_of_attempts):
    x = random.uniform(WIDTH/2 - SIZE/2, WIDTH/2 + SIZE/2)
    y = random.uniform(HEIGHT/2 - SIZE/2, HEIGHT/2 + SIZE/2)
    dart = GOval(x- DART_SIZE/2, y - DART_SIZE/2, DART_SIZE, DART_SIZE)
    distance_to_center =math.sqrt((x - WIDTH/2)**2 + (y - HEIGHT/2)**2)
    if distance_to_center < SIZE /2:
        dart.set_fill_color("red")
        successful_strike +=1
    else:
      dart.set_fill_color("blue")  
    dart.set_filled(True)
    gw.add(dart)

print(successful_strike / num_of_attempts * 4 )
