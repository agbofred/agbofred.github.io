import random
from pgl import GWindow, GOval, GRect, GLabel, GLine

gw = GWindow(800, 500)

rec = GRect(20,30, 400,200)
rec.set_fill_color('red')
rec.set_filled(True)

face =GOval(250,200, 200,200)
face.set_fill_color("yellow")
face.set_filled(True)
lefteye= GOval(280,230, 50,50)
#lefteye.set_fill_color("black")
lefteye.set_filled(True)
righteye= GOval(360,230, 50,50)
#lefteye.set_fill_color("black")
righteye.set_filled(True)

mouth = GLine(320,310,360,310)
mouth.set_line_width(4)


gw.add(rec)
gw.add(face)
gw.add(lefteye)
gw.add(righteye)
gw.add(mouth)

