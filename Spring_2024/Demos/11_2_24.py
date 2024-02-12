	
from pgl import GWindow, GRect
 
GW_WIDTH = 500
GW_HEIGHT = 200
 
gw = GWindow(GW_WIDTH, GW_HEIGHT)
rect = GRect(150, 50 ,200, 100)
rect.set_color("Blue")
rect.set_filled(True)
gw.add(rect)