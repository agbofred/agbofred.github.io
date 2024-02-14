from pgl import GWindow, GOval, GLine, GRect, GLabel
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
label = GLabel(caption, gw.get_height()/4, gw.get_height()-5)
label.set_color("red")
gw.add(label)