
from pgl import GWindow, GOval, GRect

WIDTH = 800
HEIGHT = 400
HSCALING = 1.25
VSCALING = 1.5

CX = WIDTH / 2
CY = HEIGHT / 2

gw = GWindow(WIDTH, HEIGHT)

sky = GRect(0,0, WIDTH, HEIGHT)
sky.set_filled(True)
sky.set_color('SkyBlue')
gw.add(sky)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'skyblue']
for i,c in enumerate(colors):
    NW = HSCALING * WIDTH - 20 * i
    NH = VSCALING * HEIGHT - 20 * i
    arc = GOval(CX-NW/ 2, 40 + 20 * i, NW, NH)
    arc.set_filled(True)
    arc.set_color(c)
    gw.add(arc)
