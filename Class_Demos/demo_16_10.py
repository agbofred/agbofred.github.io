from pgl import GWindow, GOval, GLine, GRect, GLabel, GArc, GPolygon, GCompound
from  G_helper import create_filled_rect, circle
GWIDTH = 500
GHEIGHT =500
def drawrc():
    
    gw = GWindow(GWIDTH,GHEIGHT)
    rec = GRect(0,0, GWIDTH,GHEIGHT)
    rec.set_fill_color("light blue")
    rec.set_filled(True)
    gw.add(rec)
    arc = GArc(50, 50, GWIDTH-80, GHEIGHT, 0, 180)
    arc.set_color("yellow")
    arc.set_filled(True)
    gw.add(arc)

#Create Triangle With Polygon
    def create_triangle(b, h):
        tri = GPolygon()
        tri.add_vertex(-b / 2, h / 2)
        tri.add_vertex(b / 2, h / 2)
        tri.add_vertex(0, -h / 2)
        return tri
    triangle = create_triangle(150, 150)
    triangle.set_filled(True)
    triangle.set_color("pink")
    #gw.add(triangle, GWIDTH/2, GHEIGHT/2)
    
    
    for i in range(5):
        x= 180 + 40*i
        y = 60-i
        triangle = create_triangle(50, 50)
        triangle.set_filled(True)
        triangle.set_color("yellow")
        #gw.add(triangle, x, y)
   
    def drawDiamond_v(): # Diamond with vertex 
        pol = GPolygon()
        pol.add_vertex(-50, 0)
        pol.add_vertex(0, 50)
        pol.add_vertex(50, -0)
        pol.add_vertex(0, -50)
        return pol
    

    def drawDiamond_e(): # Diamond with vertex 
        pol = GPolygon()
        pol.add_vertex(-50, 0)# Must be added first
        pol.add_edge(-50, 50)
        pol.add_edge(50, 50)
        pol.add_edge(50, -50)
        pol.add_edge(-50,-50)
        return pol
    

    diamond = drawDiamond_e()
    diamond.set_fill_color("green")
    diamond.set_filled(True)
    #gw.add(diamond,GWIDTH/2, GHEIGHT/2)





if __name__ == "__main__":
    drawrc()