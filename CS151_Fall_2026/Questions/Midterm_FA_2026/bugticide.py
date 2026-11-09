
from pgl import GWindow, GPolygon, GRect, GOval, GCompound
import random

WIDTH = 800
HEIGHT = WIDTH // 1.5

def paint_it_black():
    """Adds a background to the scene."""
    bg = GRect(0, 0, WIDTH, HEIGHT)
    bg.set_filled(True)
    bg.set_fill_color("#A1E2E4")
    gw.add(bg)
    return bg # this object might help you to check so that your click event do not remove background 
    
def r_color():
    """ Allowing the bug to pick random color for the head and tail """
    c ="#"
    for i in range(6):
        value = random.choice("0123456789ABCDEF")
        c +=value
    return c

def create_bug():
    """ Creates the bug and return it"""
    tail = GPolygon()
    tail.add_vertex(0,0)
    tail.add_edge(-38, 30)
    tail.add_edge(38, 30)
    tail.set_color(r_color())
    tail.set_filled(True)
    
    head = GOval(62,62)
    head.set_filled(True)
    head.set_color(r_color())
    
    bug = GCompound()
    bug.add(tail, 30, 1)
    bug.add(head, 2, 0)
    return bug

def infest(value):
    """Fills the window with bugs at random positions.

    Each bug is created with random colors and placed so that it
    lies completely inside the window.

    Inputs:
        value (int): the number of bugs to add to the window
    Outputs:
        None
    """
    bug = create_bug()
    for i in range(value):
        bug = create_bug()
        dx = random.uniform(0, WIDTH - bug.get_width())
        dy = random.uniform(0, HEIGHT - bug.get_height())
        gw.add(bug, dx, dy)
        
        
def killbug(e):
    """Removes the bug that was clicked on from the window.

    Clicks on the background, or on empty space, do nothing.
    This is the callback for the window's "click" event.

    Inputs:
        e (GMouseEvent): the click event, which gives the mouse position
    Outputs:
        None
    """
    obj = gw.get_element_at(e.get_x(), e.get_y())
    if obj is not None and obj is not gw.background:
        gw.remove(obj)
        
    ### Alternatively
    # if obj.contains(e.get_x(), e.get_y()) and obj is not None and obj is not gw.background:
    #     gw.remove(obj)
   
if __name__ == '__main__':
    gw = GWindow(WIDTH, HEIGHT)
    gw.background = paint_it_black()
    infest(25)
    gw.add_event_listener("click", killbug)