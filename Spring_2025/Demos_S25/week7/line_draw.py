from pgl import GWindow, GOval, GLine

def draw_line():
    def mouse_down(e):
        x = e.get_x()
        y = e.get_y()
        gw.line =GLine(x,y,x,y)
        gw.add(gw.line)
    def mouse_drag(e):
        gw.line.set_end_point(e.get_x(), e.get_y())
    
    gw = GWindow(500,500)
    gw.line = None
    gw.add_event_listener("mousedown", mouse_down)
    gw.add_event_listener("drag", mouse_drag)
draw_line()
    