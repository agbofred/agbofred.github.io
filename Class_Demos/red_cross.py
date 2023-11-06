from pgl import GWindow, GCompound, GRect, GState
import random
def make_cross():
    cross = GCompound ()
    hrec = GRect(60, 20)
    hrec.set_filled(True)
    hrec.set_color("Red")
    cross.add(hrec, -hrec.get_width()/2, -hrec.get_height()/2)
    vrec = GRect (20, 60)
    vrec.set_filled(True)
    vrec.set_color("Red")
    cross.add(vrec , -vrec.get_width()/2, -vrec.get_height()/2)
    return cross
def move():
    cross.move_polar(2, gs.angle)
def click (e):
    x = e.get_x()
    y = e.get_y()
    if gw.get_element_at(x,y) is not None :
        gs.angle = random.randint(0,360)
gw = GWindow(200,200) # Size doesn 't matter here apparently
gs = GState()
gs.angle = random.randint(0,360)
cross = make_cross()
gw.add(cross , gw.get_width()/2, gw.get_height()/2)
gw.set_interval (move , 20)
gw.add_event_listener ("click", click)