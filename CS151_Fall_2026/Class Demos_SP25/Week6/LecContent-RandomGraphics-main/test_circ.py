from pgl_tools import create_filled_circ
from pgl import GWindow


WIDTH = 300
HEIGHT = 400

gw = GWindow(WIDTH, HEIGHT)

cir1 = create_filled_circ(WIDTH, HEIGHT, 50, True, True, "red")
cir2 = create_filled_circ(WIDTH, HEIGHT, 25, True, True, "grey")

gw.add(cir1)
gw.add(cir2)
