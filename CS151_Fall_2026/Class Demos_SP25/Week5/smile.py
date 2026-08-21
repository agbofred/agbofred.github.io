from pgl import GWindow, GOval, GRect, GLabel, GLine
G_WIDTH =400
G_HEIGHT =400
def draw_smilly_face(): # This function is drawing the smilly face
    gw = GWindow(G_WIDTH, G_HEIGHT) 

    # Create a head 
    head =GOval(100, 100, 200, 200)
    head.set_fill_color("yellow")
    head.set_filled(True)
    gw.add(head)

    # Create left eye
    l_eye = GOval(150, 140, 33,30)
    l_eye.set_filled(True)
    gw.add(l_eye)

       # Create right eye
    r_eye = GOval(220, 140, 33,30)
    r_eye.set_filled(True)
    gw.add(r_eye)

    # create mouth
    mouth = GLine(160,200,250,200)
    mouth.set_line_width(5)
    gw.add(mouth)

    #create caption
    caption =GLabel("This is the smilly face from CS151", 100,320)
    caption.set_color("green")
    gw.add(caption)

if __name__ == "__main__":
    draw_smilly_face()
