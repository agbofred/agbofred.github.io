import random
from pgl import GArc, GWindow, GRect, GLabel, GLine, GOval
GWINDOW_WIDTH = 400
GWINDOW_HEIGHT = 400

def draw_centere_line():
    gw = GWindow(500, 200)
    msg = GLabel("hello world!")
    msg.set_font("italic bold 20px 'times new roman'")
    x = 250 - msg.get_width() / 2
    y = 100 + msg.get_ascent() / 2
    gw.add(msg, x, y)

def oval():
    ov = GOval(120, 100, 30,30)
    ov.get_fill_color("red")
    ov.set_filled(True)
    gw.add(ov)

    rec = GRect(20,20, 100,120)
    gw.add(rec)

if __name__ == "__main__":
    #draw_over()
    #draw_checker()
    draw_centere_line()
