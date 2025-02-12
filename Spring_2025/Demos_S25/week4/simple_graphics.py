from pgl import GWindow, GRect
import random

li = ["doe", "bell", 4, {5,6,7}, "Fred"]
random.shuffle(li)

#print(li)

GW_WIDTH = 500
GW_HIEGHT = 500

gw =GWindow(GW_WIDTH, GW_WIDTH)

rectangle = GRect(200, 200, 100, 100)
rectangle.set_color("red")
rectangle.set_filled(True)
gw.add(rectangle)