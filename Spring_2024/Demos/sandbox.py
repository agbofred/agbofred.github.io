from pgl import GWindow, GOval, GLine, GRect, GLabel, GArc
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

def filled_arc():
    gw = GWindow(400, 400)
    arc = GArc(50, 50, 
               350, 350, 
               90, 135)
    arc.set_color("orange")
    arc.set_filled(True)
    gw.add(arc)
filled_arc()