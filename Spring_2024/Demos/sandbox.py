from pgl import GWindow, GOval, GLine, GRect, GLabel
gw = GWindow(500, 200)
msg = GLabel("hello world!")
msg.set_font("italic bold 20px 'times new roman'")
x = 250 - msg.get_width() / 2
y = 100 + msg.get_ascent() / 2
gw.add(msg, x, y)