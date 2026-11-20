from pgl import GWindow, GPolygon, GRect, GOval, GCompound
import random

WIDTH = 800
HEIGHT = WIDTH // 1.5

def paint_it_black():
    """Adds a light blue background (the city map) to the scene."""
    bg = GRect(0, 0, WIDTH, HEIGHT)
    bg.set_filled(True)
    bg.set_fill_color("#A1E2E4")
    gw.add(bg)
    return bg 
    


def r_color():
    """Returns a random color string such as "#3FA9C2"."""
    c = "#"
    for i in range(6):
        c += random.choice("0123456789ABCDEF")
    return c


def create_bug():
    """Creates ONE bug and returns it (it is NOT added to the window).

    The bug is a GCompound made of a tail and a head. Its top-left
    corner is at (0, 0) inside the compound, so once it is added to
    the window at (x, y) its top-left corner is at (x, y).
    Its size is about 77 pixels wide and 62 pixels tall.

    Outputs:
        (GCompound): the bug
    """
    tail = GPolygon()
    tail.add_vertex(0, 0)
    tail.add_polar_edge(120, 120)
    tail.add_polar_edge(120, 0)
    # tail.add_edge(-38, 30)
    # tail.add_edge(38, 30)
    tail.set_color(r_color())
    tail.set_filled(True)

    head = GOval(62, 62)
    head.set_filled(True)
    head.set_color(r_color())

    bug = GCompound()
    bug.add(tail, 38, 1)
    # bug.add(head, 15, 0)
    return bug


gw = GWindow(WIDTH, HEIGHT)
paint_it_black()
gw.add(create_bug(), WIDTH//2, HEIGHT//2)