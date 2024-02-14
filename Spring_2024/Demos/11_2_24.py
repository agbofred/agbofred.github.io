from pgl import GWindow, GRect,GOval
import random
 
GW_WIDTH =1000
GW_HEIGHT = 600
 
gw = GWindow(GW_WIDTH, GW_HEIGHT)

def create_bubble(size):
    dx = random.randint(10, GW_WIDTH)
    dy = random.randint(GW_HEIGHT//2-10, GW_WIDTH//2-20)
    bubble = GOval(dx,dy, 100-(size*2),100-(size-2))
    bubble.set_color(color())
    bubble.set_filled(True)
    bubble.get_x()
    return gw.add(bubble)

def color():
    code ="#"
    for i in range(6):
        code += random.choice("123456789ABCDEF")
    return code

for i in range(1,100,2):
    create_bubble(i)