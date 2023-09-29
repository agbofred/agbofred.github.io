import random
from pgl import GArc, GWindow, GRect, GLabel, GLine, GOval
GWINDOW_WIDTH = 400
GWINDOW_HEIGHT = 400

def draw_over():
    gw = GWindow(GWINDOW_WIDTH,GWINDOW_HEIGHT)
    message =GLabel("Hello Graphics", 100, 100)
    oval = GOval(20,20,350,350)
    
    oval.set_filled(True)
    oval.set_fill_color("yellow")
    lefteye = GOval(100,100, 30,30)
    lefteye.set_filled(True)
    righteye = GOval(250,100, 30,30)
    righteye.set_filled(True)
    mouth = GLine(150,220, 220, 220)
    mouth.set_line_width(4)
    #gw.add(message)
    gw.add(oval)
    gw.add(lefteye)
    gw.add(righteye)
    gw.add(mouth)

def draw_checker():
    gw = GWindow(200,200)
    for c in range(0,10):
        for r in range(0,10):
            rect = GRect(20*c,20*r,20,20)
            if (r+c) % 2 != 0:
                rect.set_filled(True)
            gw.add(rect)

def draw_centere_line():
    gw = GWindow(500, 200)
    msg = GLabel("hello world!")
    msg.set_font("italic bold 20px 'times new roman'")
    x = 250 - msg.get_width() / 2
    y = 100 + msg.get_ascent() / 2
    gw.add(msg, x, y)

if __name__ == "__main__":
    #draw_over()
    #draw_checker()
    draw_centere_line()



"""s = "ABCdef"
for ch in s:
    if s.rfind(ch)>0:
        print(ch)
"""