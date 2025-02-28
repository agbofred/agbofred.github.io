from pgl import GWindow, GOval, GLine, GRect, GLabel, GArc, GPolygon, GCompound
#from  G_helper import create_filled_rect, circle
GWIDTH = 500
GHEIGHT =500
# Drawing an arc starting from angle 0 degree and sweep until 180 degree
def drawrc():
    
    """gw = GWindow(GWIDTH,GHEIGHT)
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
    gw.add(triangle, GWIDTH/2, GHEIGHT/2)
    
    # attempting to create a sun-like spike
    for i in range(5):
        x= 180 + 40*i
        y = 60-i
        triangle = create_triangle(50, 50)
        triangle.set_filled(True)
        triangle.set_color("yellow")
        gw.add(triangle, x, y)
   
    #Drawing Diamond shape with GPolygon
    def drawDiamond_v(): # Diamond with vertex 
        pol = GPolygon()
        pol.add_vertex(-50, 0)
        pol.add_vertex(0, 50)
        pol.add_vertex(50, -0)
        pol.add_vertex(0, -50)
        return pol
    

    def drawDiamond_edge(): # Diamond with edges 
        pol = GPolygon()
        pol.add_vertex(-50, 0)# Must be added first
        pol.add_edge(-50, 50)
        pol.add_edge(50, 50)
        pol.add_edge(50, -50)
        pol.add_edge(-50,-50)
        return pol
    

    diamond = drawDiamond_edge()
    diamond.set_fill_color("#00FFAF06")
    diamond.set_filled(True)
    #gw.add(diamond,GWIDTH/2, GHEIGHT/2)"""

gw = GWindow(GWIDTH,GHEIGHT)
rec = GRect(0,0, GWIDTH,GHEIGHT)
rec.set_fill_color("light blue")
rec.set_filled(True)
gw.add(rec)
arc = GArc(10, 10, GWIDTH-100, GHEIGHT-100, 90, 120)
arc.set_color("yellow")
arc.set_filled(True)
gw.add(arc)

# attempting to create a sun-like spike
"""for i in range(5):
    x= 180 + 40*i
    y = 60-i
    triangle = create_triangle(50, 50)
    triangle.set_filled(True)
    triangle.set_color("yellow")
    #gw.add(triangle, x, y)"""


#Create Triangle With Polygon
def create_triangle(b, h):
    tri = GPolygon()
    tri.add_vertex(b/2, 0)
    tri.add_vertex(0, h)
    tri.add_vertex(b, h)
    return tri
triangle = create_triangle(150, 150)
triangle.set_filled(True)
triangle.set_color("pink")
gw.add(triangle, GWIDTH/2, GHEIGHT/2)


#Drawing Diamond shape with GPolygon
def drawDiamond_v(): # Diamond with vertex 
    pol = GPolygon()
    pol.add_vertex(-50, 0)
    pol.add_vertex(0, 50)
    pol.add_vertex(50, 0)
    pol.add_vertex(0, -50)
    return pol


def drawDiamond_edge(): # Diamond with edges 
    pol = GPolygon()
    pol.add_vertex(-100, 0)# Must be added first
    pol.add_edge(-100, 100)
    pol.add_edge(100, 100)
    pol.add_edge(100, -100)
    pol.add_edge(-100,-100)
    return pol


diamond = drawDiamond_edge()
diamond.set_fill_color("white")
diamond.set_filled(True)
#gw.add(diamond,GWIDTH/2, GHEIGHT/2)

#Hexagon by Polar_Edge
def triangle_by_polar_edge():
    def create_eq_triangle(side):
        tri = GPolygon()
        tri.add_vertex(0, 0)
        for i in range(0, 360, 120):
            tri.add_polar_edge(side, i)
        return tri

    gw = GWindow(500, 500)
    triangle = create_eq_triangle(100)
    triangle.set_filled(True)
    triangle.set_color("green")
    gw.add(triangle, 250, 250)

triangle_by_polar_edge()



#--------AXE

def my_axe():
    def create_axe():
        axe = GCompound()
        shaft = GRect(-15, 0, 30, 300)
        shaft.set_filled(True)
        shaft.set_color("brown")
        axe.add(shaft)

        blade = GPolygon()
        blade.add_vertex(0, 0)
        blade.add_vertex(200, -50)
        blade.add_vertex(200, 50)
        blade.set_filled(True)
        blade.set_color("#0020AF66")
        axe.add(blade, -80, 50)
        return axe

    gw = GWindow(500, 500)
    axe = create_axe()
    gw.add(axe, 250, 100)


if __name__ == "__main__":
    pass
    #arc(150)
    #create_triangle(200,200)
    triangle_by_polar_edge()
    #drawrc()
    #my_axe()