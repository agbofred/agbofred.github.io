from pgl import GWindow, GOval, GLine, GRect, GLabel, GArc, GPolygon
from  G_helper import create_filled_rect, circle
import random
"""s="string"
print(s[1:5])
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(a[12:15:2]+a[18::5]+ a[-8]) # Answer is NOSXY

print((9 - 3) + 25%5 +3 * 4- 1*(4 - 3 ** 3 + 5) +23 // 7)
print(not (12 < 6 - 5 or 9 // 3 == 3))

def func(a, b=5, c= True):
    if c:
        return a + c
    else:
        return a * b
print(func(5,True,False))"""
GWIDTH = 500
GHEIGHT =500


def clickable_anumate():
    gw = GWindow(GWIDTH, GHEIGHT)
    #def step():

    def clickdisplay(e):
        px = random.randint(GWIDTH- e.get_x()/2, GHEIGHT- e.get_y()/2)
        py = random.randint(GWIDTH- e.get_x()/2, GHEIGHT- e.get_y()/2)
        rec=create_filled_rect(px, py, 20, 20, color())
        rec.move(px,py)
        print(px)
        
        

    """def drawsq():
        rec = create_filled_rect(getX(), getY(), 20, 20, color())
        return rec"""
    def getX():
        x= random.randint(gw.get_width()/2, gw.get_height()/2)
        return x
    def getY():
        y= random.randint(gw.get_width()/2, gw.get_height()/2)
        return y
    def color():
        c="#"
        for i in range(6):
            c += random.choice("0123456789ABCDEF")
        return c
    gw.add_event_listener("click", clickdisplay)
    rec=  rec = create_filled_rect(getX(), getY(), 20, 20, color())
    gw.add(rec)

def createDiamond():
    pol_height = 120
    pol = GPolygon()
    pol.add_vertex(-pol_height, 0)
    #pol.add_vertex(0, pol_height/2)
    pol.add_vertex(pol_height/2, 0)
    pol.add_vertex(0, -pol_height)
    #pol.add_vertex(0, pol_height/2)
    gw = GWindow(GWIDTH, GHEIGHT)
    gw.add(pol, gw.get_width()/2, gw.get_height()/2)

def triangle_by_vertex():
    def create_triangle(b, h):
        tri = GPolygon()
        tri.add_vertex(-b / 2, h / 2)
        tri.add_vertex(b / 2, h / 2)
        tri.add_vertex(0, -h / 2)
        return tri

    gw = GWindow(500, 500)
    triangle = create_triangle(200, 200)
    triangle.set_filled(True)
    triangle.set_color("red")
    gw.add(triangle, 250, 250)

def rainbow():
    HSCALING = 1.25
    VSCALING = 1.5
    gw = GWindow(GWIDTH,GHEIGHT)
    rec = GRect(0,0, GWIDTH,GHEIGHT)
    rec.set_fill_color("light blue")
    rec.set_filled(True)
    gw.add(rec)
    color = ["Red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for i,c in enumerate(color):
        NW = HSCALING * GWIDTH - 20 * i
        NH = VSCALING * GHEIGHT - 20 * i
        arc = GArc(20*i, 50/2*i, NW, NH, 0, 180)
        arc.set_color(c)
        arc.set_filled(True)
        gw.add(arc)

    

if __name__ == "__main__":
    #clickable_anumate()
    #createDiamond()
    #triangle_by_vertex()
    rainbow()
