"""
Recreating a flag of your choice!
"""

from pgl import GWindow, GRect, GOval


WIDTH = 600
HEIGHT = 400

gw = GWindow(WIDTH, HEIGHT)
bar1 = GRect((WIDTH/2)-100, (HEIGHT/2)-100, 100,200)
bar2 = GRect((WIDTH/2)-0, (HEIGHT/2)-100, 100,200)
bar3 = GRect((WIDTH/2)+100, (HEIGHT/2)-100, 100,200)
pole = GRect((WIDTH/2)-100, (HEIGHT/2)+100, 10, 200)

# Color the bars
bar1.set_color("blue")
bar1.set_filled(True)
bar2.set_color("white")
bar2.set_filled(True)
bar3.set_color("red")
bar3.set_filled(True)
pole.set_color("black")
pole.set_filled(True)

gw.add(bar1)
gw.add(bar2)
gw.add(bar3)
gw.add(pole)

