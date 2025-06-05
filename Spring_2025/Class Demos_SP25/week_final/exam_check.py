from pgl import GWindow, GArc, GCompound, GOval
COLORS = ["red", "green", "blue", "orange"] #colors
GW_WIDTH = 500 # width of window
GW_HEIGHT = 500 # height of window
CHART_RADIUS = 150 # radius of pie chart
HIGHLIGHT_THICKNESS = 10 # line thickness when clicked
CHART_SIZE = 100

def create_pie_chart(list_of_percents):

    #This is how you first add each slice to the gwindow

    def create_slice(start, end, color):

         s = GArc(100, 100, CHART_RADIUS * 2, CHART_RADIUS * 2, start, end)

         #Set it equal to the index of the next color

         s.set_fill_color(COLORS[color])

         s.set_filled(True)

         s.set_location(CHART_RADIUS + 100, CHART_RADIUS + 100)

         #Starting angle is 0 at the beginning of the function

    start =  0

    for x in range(len(list_of_percents)):

         #End equals start + the angle amount of the current slice

         end = start + list_of_percents[x] * 3.6

         #color = an index of the color we want

         color = x % len(list_of_percents)

         #Create a slice at the start, end, and we also give the index of what color we want

         create_slice(start, end, color)

         #Next time in the for loop, start becomes where end is currently

         start += list_of_percents[x] * 3.6

    def highlight(mouse):

         #If we mouse down somewhere, we get whatever element is there and set the line width

        if gw.get_element_at(mouse.get_x(), mouse.get_y()) is not None:

            arc = gw.get_element_at(mouse.get_x(), mouse.get_y())

            arc.set_line_width(HIGHLIGHT_THICKNESS)

            gw.add(arc)

    def unhighlight():

         #Get the variable arc from our highlight function, then set the line width

         global arc

         arc.set_line_width(0)

    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    gw.add_event_listener("mousedown", highlight)

    gw.add_event_listener("mouseup", unhighlight)

    

    

    

if __name__ == "__main__":

    create_pie_chart([50,30,20])
#create_pie_chart([50,30,20])