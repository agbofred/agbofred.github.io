from english import ENGLISH_WORDS, is_english_word
from pgl import GWindow, GLine, GRect, GOval
from G_helper import circle

import math
GW_WIDTH = 500
GW_HEIGHT = 500
RADIUS = 10

## Drawing dots on click
def interactDrawDot():

    def click_action(e): # event when mouse clicks
        gw.add(circle(e.get_x(), e.get_y(),RADIUS,"black"))
    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    gw.add_event_listener("click", click_action)
    
## Drawing a line on window
def drawline():
    gw= GWindow(GW_WIDTH, GW_HEIGHT)

    def mousedown_action(e): # event when mose is down
        gw.lin = GLine(e.get_x(),e.get_y(), e.get_x(), e.get_y())
        gw.add(gw.lin)

    def mouse_drag_action(e):
        gw.lin.set_end_point(e.get_x(), e.get_y())
    ## Adding event listener to the window, allowing it listen to actions of events
    gw.add_event_listener("mousedown", mousedown_action)
    gw.add_event_listener("drag", mouse_drag_action)  

# Creat a dragable rectangle

def drawRectangle():
    gw= GWindow(GW_WIDTH, GW_HEIGHT)
    rec = GRect(400, 200, 50,50)
    rec.set_fill_color("red")
    rec.set_filled(True)
    gw.add(rec)


    def mouseD(e): # getting the coordinate of the object
        gw.last_x = e.get_x()
        gw.last_y = e.get_y()
        gw.gobj = gw.get_element_at(gw.last_x, gw.last_y)
    
    def dragrec(e): # placing the object in another location
        if gw.gobj is not None:
            gw.gobj.move(e.get_x()-gw.last_x, e.get_y()- gw.last_y)
            gw.last_x = e.get_x()
            gw.last_y = e.get_y()
    gw.add_event_listener("mousedown", mouseD)
    gw.add_event_listener("drag", dragrec)



if __name__ == "__main__":
    #interactDrawDot()
    #creatFilledCircle(200,200,"red")
    #drawline()
    drawRectangle()



""" Make oval"""

"""def creatFilledCircle(x,y,r,fill):
    oval = GOval(x-r,y-r,2*r,2*r)
    oval.set_color(fill)
    oval.set_filled(True)
    #gw = GWindow(GW_WIDTH,GW_HEIGHT)
    #gw.add(oval)
    return oval"""

""" Make Circles """

"""def make_circle(x,y,r):
    c = GOval(x-r, y-r, 2*r, 2*r)
    c.set_filled(True)
    if randint(1, 100) > 75:
        c.set_color("#F92672") #pink
    else:
        c.set_color("#66D9EF") #blue
    return c

gw = GWindow(500, 500)
for i in range(50):
    gw.add(make_circle(
            randint(50,450), 
            randint(50,450), 
            randint(5,50)
            )
          )"""