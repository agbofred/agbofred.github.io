from pgl import GWindow, GRect
import random

gw = GWindow(500, 500)
rec = GRect(10,0, 100, 100)
rec.set_color("red")
rec.set_filled(True)
gw.add(rec)
