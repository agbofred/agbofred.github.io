from pgl import GWindow, GOval, GLine, GRect, GLabel
import random

def draw_emoji():
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
    mouth.set_line_width(15)
    gw.add(mouth)


    # Makeing right and left pupil
    lpupil = GOval(120, 110, 20, 15)
    lpupil.set_fill_color("white")
    lpupil.set_filled(True)
    gw.add(lpupil)


    rpupil = GOval(260, 110, 20, 15)
    rpupil.set_fill_color("white")
    rpupil.set_filled(True)
    gw.add(rpupil)

    # Giving the image a lable
    caption = "This is a pumpkin head!"
    label = GLabel(caption, 100, gw.get_height()-5)
    label.set_color("green")
    gw.add(label)

    def move_eye(event):
        #lradius = lpupil.get_width()/2
        #rradius = rpupil.get_width()/2
        lpupil.move_polar(0.04, event.get_x()) #0.03
        rpupil.move_polar(0.04, event.get_x())
        #lpupil.move_polar(leye.get_width()/200, event.get_y())
        #rpupil.move_polar(reye.get_width()/200, event.get_y())
  
    gw.add_event_listener("mousemove",move_eye)


if __name__ =='__main__':
    draw_emoji()