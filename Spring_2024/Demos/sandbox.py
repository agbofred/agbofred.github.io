from pgl import GWindow, GOval, GLine, GRect, GLabel, GArc, GPolygon
import random
"""
def make_filled_circ(x_cent, y_cent, radius, color='black'):
    circle = GOval(x_cent-radius, y_cent-radius, 2*radius, 2*radius)
    circle.set_color(color)
    circle.set_filled(True)
    return circle
if __name__ =="__main__":
    gw = GWindow(800, 600)
    c1= make_filled_circ(200,200, 20,"green")
    gw.add(c1)
    c2= make_filled_circ(300,300, 40,"red")
    gw.add(c2)
    c3= make_filled_circ(200,200, 10,"white")
    gw.add(c3)


#------------------------Clicking event program----------
def draw_dots():
    def click_action(event):
        c = create_filled_rect(
            event.get_x(), event.get_y(), 
            10,10, random_color())
        gw.add(c)

    def create_filled_rect(x,y,w,h,color):
        rec = GRect(x,y,w,h)
        rec.set_color(color)
        rec.set_filled(True)
        return rec
    def random_color():
        color ="#"
        for i in range(6):
            color += random.choice("123456789ABCDEF")
        return color

    gw = GWindow(500, 500)
    gw.add_event_listener("click", click_action)

if __name__ =="__main__":
   draw_dots()"""
GWIDTH = 600
GHEIGHT = 600
gw = GWindow(GWIDTH,GHEIGHT)
#Create Triangle With Polygon
def create_triangle(w,h):
    tri = GPolygon()
    #tri.add_vertex(0,0)
    tri.add_vertex(h/2,w/2)
    tri.add_vertex(-w/2, h/2)
    tri.add_vertex(0,-h/2)

    tri.set_filled(True)
    tri.set_color("pink")
    gw.add(tri, GWIDTH/2, GHEIGHT/2)

create_triangle(150,150)


def create_hexagon(side):
    hex = GPolygon()
    hex.add_vertex(-side, 0)
    angle = 60
    for i in range(6):
        hex.add_polar_edge(side, angle)
        angle -= 60
    return gw.add(hex, 100, 100)
#create_hexagon(40)