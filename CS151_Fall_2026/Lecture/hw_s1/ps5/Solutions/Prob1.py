# A part
def create_histogram_array(imax, list):
    table = [0]*imax
    for i in range(imax):
        for item in range(len(list)):
            if i == list[item]:
                table[i] += 1
    return table 

print(create_histogram_array(5,[1, 0, 3, 2, 4, 2, 2, 1, 3, 0]))

#B part

def print_histogram(array):
    for i in range(len(array)):
        print(f'{i}:{"*"*array[i]}')

print(print_histogram(create_histogram_array(5,[1, 0, 3, 2, 4, 2, 2, 1, 3, 0])))

#C Part
from pgl import GWindow, GRect, GCompound
def create_histogram_graph(array, width, height):
    comparray = GCompound()
    bar_width = width//len(array)
    for i in range(len(array)):
        bar_height = 100*array[i]
        #print(width, height)
        bar =GRect((bar_width*i)+ bar_width, bar_width, bar_width, bar_height)
        bar.set_fill_color("red")
        bar.set_filled(True)
        bar.rotate(180)
        comparray.add(bar)
    return comparray

def test_create_histogram_graph():
    WIDTH, HEIGHT = 800, 600
    gw = GWindow(WIDTH, HEIGHT)
    PI_DIGITS = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 5, 8, 9, 7, 9]
    array = create_histogram_array(10, PI_DIGITS)
    graph = create_histogram_graph(array, WIDTH, HEIGHT)
    gw.add(graph, 0, HEIGHT-200)

test_create_histogram_graph()