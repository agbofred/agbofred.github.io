from pgl import GWindow, GOval, GLine, GLabel, GPolygon
GWIDTH = 400
GHEIGHT = 400
HEAD_WIDTH = 360
HEAD_HEIHGT = 360

def draw_emoji():
    gw = GWindow(GWIDTH, GHEIGHT)
    head = GOval(20, 20, HEAD_WIDTH, HEAD_HEIHGT)
    head.set_fill_color("yellow")
    head.set_filled(True)
    gw.add(head)

    reye = GOval(110, 100, 40, 40)
    reye.set_filled(True)
    gw.add(reye)

    leye = GOval(250, 100, 40, 40)
    leye.set_filled(True)
    gw.add(leye)

    #Adding the nose , 150
    tri = GPolygon()
    tri.add_vertex(30/2, 0)
    tri.add_vertex(0, 30)
    tri.add_vertex(30, 30)
    tri.set_filled(True)
    gw.add(tri, HEAD_WIDTH/2, HEAD_HEIHGT/2)

    mouth = GLine(150, 250, 250, 250)
    mouth.set_line_width(15)
    gw.add(mouth)


    # Making right and left pupil
    lpupil = GOval(120, 110, 20, 15)
    lpupil.set_fill_color("white")
    lpupil.set_filled(True)
    gw.add(lpupil)


    rpupil = GOval(260, 110, 20, 15)
    rpupil.set_fill_color("white")
    rpupil.set_filled(True)
    gw.add(rpupil)

    # Left pupil movement action
    def move_leye(event):
        if (event.get_x()>0 or event.get_y()>0):
            if event.get_x() < gw.get_x_lpupil and event.get_y()> gw.get_y_lpupil :
                dx = gw.get_x_lpupil - leye.get_height()//5
                dy = gw.get_x_lpupil + leye.get_height()//25
                print(f'Leye->{dx,dy}')
                lpupil.set_location(dx,dy) 
            elif event.get_x() > gw.get_x_lpupil and event.get_y()> gw.get_y_lpupil :
                dx = gw.get_x_lpupil + leye.get_height()//5
                dy = gw.get_x_lpupil + leye.get_height()//25
                print(f'Leye->{dx,dy}')
                lpupil.set_location(dx,dy)
    
    # Right pupil movement action
    def move_reye(event):
        if (event.get_x()>0 or event.get_y()>0):
            if event.get_x() < gw.get_x_rpupil and event.get_y() > gw.get_y_rpupil :
                dx = gw.get_x_rpupil - reye.get_height()//10
                dy = gw.get_y_rpupil + reye.get_height()//3
                print(f'Reye->{dx,dy}')
                rpupil.set_location(dx,dy) 

            elif event.get_x() > gw.get_x_rpupil and event.get_y()> gw.get_y_rpupil :
                dx = gw.get_x_rpupil + reye.get_height()//5
                dy = gw.get_y_rpupil + reye.get_height()//4
                print(f'Reye->{dx,dy}')
                rpupil.set_location(dx,dy)

    # Giving the image a lable
    caption = "This is an emoji simulation of a pumpkin head!"
    label = GLabel(caption, 10, gw.get_height()-5)
    label.set_color("green")
    gw.add(label)
  
    # Adding the two event to listeners            
    gw.add_event_listener("mousemove",move_reye)
    gw.add_event_listener("mousemove",move_leye)
    
    #Setting global variables
    gw.get_x_rpupil = rpupil.get_x()
    gw.get_y_rpupil = rpupil.get_y()
    gw.get_x_lpupil = lpupil.get_x()
    gw.get_y_lpupil = lpupil.get_y()

if __name__ =='__main__':
    draw_emoji()