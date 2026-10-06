from pgl import GWindow, GLine
 
WIDTH = 500
HEIGHT = 500
 
def draw_lines():
    def mousedown_event(e):
        x = e.get_x()
        y = e.get_y()
        gw.line = GLine(x,y,x,y)
        gw.add(gw.line)
 
    def drag_action(e):
        gw.line.set_end_point(e.get_x(), e.get_y())
 
    gw = GWindow(WIDTH, HEIGHT)
    gw.line = None
    gw.add_event_listener("mousedown", mousedown_event)
    gw.add_event_listener("drag", drag_action)
 
if __name__ == '__main__':
    draw_lines()
