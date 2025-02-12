from pgl import GWindow, GRect, GOval, GLabel, GLine

gw = GWindow(400, 400)

head = GOval(20, 20, 360, 360)
head.set_fill_color("yellow")
head.set_filled(True)
gw.add(head)

reye = GOval(110, 100, 40, 40)
reye.set_filled(True)
gw.add(reye)

leye = GOval(250, 100, 40, 40)
leye.set_filled(True)
gw.add(leye)

mouth = GLine(150, 250, 250, 250)
mouth.set_line_width(5)
gw.add(mouth)


"""Another Version of the smilly face"""
from pgl import GWindow, GOval, GRect, GLabel, GLine

GW_WIDTH = 400
GW_HEIGHT = 400

def draw_smilly(): # Function to draw a smilly face
    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    head = GOval(100, 100, 200,200)
    head.set_fill_color("yellow")
    head.set_filled(True)
    gw.add(head)

    left_eye =GOval(140, 130, 50,50)
    left_eye.set_filled(True)
    gw.add(left_eye)

    right_eye =GOval(210, 130, 50,50)
    right_eye.set_filled(True)
    gw.add(right_eye)

    mouth = GLine(150, 220, 250, 220)
    mouth.set_line_width(10)
    gw.add(mouth)



if __name__ =="__main__":
    pass
    #draw_smilly()