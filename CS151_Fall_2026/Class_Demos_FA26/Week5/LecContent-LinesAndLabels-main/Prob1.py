
from pgl import GWindow, GRect, GOval, GLine
import stars


WIDTH = 600
HEIGHT = 400

def make_background():
    """Makes the dark blue background and adds it to the window"""
    bg = GRect(WIDTH, HEIGHT)
    bg.set_filled(True)
    bg.set_color('#001C46')
    gw.add(bg)

def create_star(num):
    """Creates a numbered star. Stars should be connected in the order they
    are created.

    Inputs:
        num (int): Which star to create
    Returns:
        (Goval): The star GOval object
    """
    STAR_SIZE=5
    x = stars.xs[num-1]
    y = 400 - stars.ys[num-1]
    star = GOval(x - STAR_SIZE/2, y-STAR_SIZE/2, STAR_SIZE, STAR_SIZE)
    star.set_filled(True)
    star.set_color('white')
    return star


gw = GWindow(WIDTH, HEIGHT)
make_background()
star1 = create_star(1)
star2 = create_star(2)
star3 = create_star(3)
star4 = create_star(4)
star5 = create_star(5)
star6 = create_star(6)
star7 = create_star(7)

gw.add(star1)
gw.add(star2)
gw.add(star3)
gw.add(star4)
gw.add(star5)
gw.add(star6)
gw.add(star7)


