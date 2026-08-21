from pgl import GWindow, GOval, GLine, GLabel, GPolygon
GWIDTH = 400
GHEIGHT = 400
HEAD_WIDTH = 360
HEAD_HEIHGT = 360
EYE_RADIUS = 25
PUPIL_RADIUS = EYE_RADIUS / 2

def draw_emoji():
    gw = GWindow(GWIDTH, GHEIGHT)
    head = GOval(20, 20, HEAD_WIDTH, HEAD_HEIHGT)
    head.set_fill_color("yellow")
    head.set_filled(True)
    gw.add(head)

    #Making right and left eyes
    reye = GOval(2 * EYE_RADIUS, 2 * EYE_RADIUS)
    reye.set_filled(True)
    gw.add(reye, GWIDTH / 2 + 2 * EYE_RADIUS - EYE_RADIUS, GHEIGHT / 3 - EYE_RADIUS)

    leye = GOval(2 * EYE_RADIUS, 2 * EYE_RADIUS)
    leye.set_filled(True)
    gw.add(leye, GWIDTH / 2 - 2 * EYE_RADIUS - EYE_RADIUS, GHEIGHT / 3 - EYE_RADIUS)

    #Adding the nose , 150
    tri = GPolygon()
    tri.add_vertex(30/2, 0)
    tri.add_vertex(0, 30)
    tri.add_vertex(30, 30)
    tri.set_filled(True)
    gw.add(tri, HEAD_WIDTH/2, HEAD_HEIHGT/2)

    mouth = GLine(150, 280, 250, 280)
    mouth.set_line_width(10)
    gw.add(mouth)

    # Making right and left pupil
    lpupil = GOval(2 * PUPIL_RADIUS, 2 * PUPIL_RADIUS)
    lpupil.set_fill_color("white")
    lpupil.set_filled(True)
    gw.add(lpupil, GWIDTH / 2 - 2 * EYE_RADIUS - PUPIL_RADIUS, GHEIGHT / 3 - PUPIL_RADIUS)

    rpupil = GOval(2 * PUPIL_RADIUS, 2 * PUPIL_RADIUS)
    rpupil.set_fill_color("white")
    rpupil.set_filled(True)
    gw.add(rpupil, GWIDTH / 2 + 2 * EYE_RADIUS - PUPIL_RADIUS, GHEIGHT / 3 - PUPIL_RADIUS)

    """ Implementation of pupil movement by setting the call bac function named move_action"""
    def compute_displacement(eye_x, eye_y, mouse_x, mouse_y, move_dist):
        dx = mouse_x - eye_x
        dy = mouse_y - eye_y
        dist = (dx**2 + dy**2) ** (1 / 2)
        sx = move_dist * dx / dist
        sy = move_dist * dy / dist
        return sx, sy

    def move_action(event):
        mx, my = event.get_x(), event.get_y()
        lx, ly = GWIDTH / 2 - 2 * EYE_RADIUS, GHEIGHT / 3
        rx, ry = GWIDTH / 2 + 2 * EYE_RADIUS, GHEIGHT / 3
        lsx, lsy = compute_displacement(lx, ly, mx, my, PUPIL_RADIUS)
        rsx, rsy = compute_displacement(rx, ry, mx, my, PUPIL_RADIUS)
        lpupil.set_location(lx + lsx - PUPIL_RADIUS, ly + lsy - PUPIL_RADIUS)
        rpupil.set_location(rx + rsx - PUPIL_RADIUS, ry + rsy - PUPIL_RADIUS)

    # Giving the image a lable
    caption = "This is an emoji simulation of a pumpkin head!"
    label = GLabel(caption, 10, gw.get_height()-5)
    label.set_color("green")
    gw.add(label)
  
    # Adding the two event to listeners            
    gw.add_event_listener("mousemove",move_action)
    

if __name__ =='__main__':
    draw_emoji()