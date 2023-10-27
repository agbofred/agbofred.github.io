from pgl import GWindow, GOval, GImage
import random

def tabulate():
    mark = [random.randint(50,100) for i in range(27) ]
    count = [0 for i in range(5)]
    for i in range(len(mark)):
        if mark[i] >= 90:
            count[0] +=1
        elif mark[i] >= 80:
            count[1] +=1
        elif mark[i] >= 70:
            count[2] +=1
        elif mark[i] >= 60:
            count[3] +=1
        else:
            count[4] +=1
    print(mark)
    print(count)
    """print(f'The Histogram of counts:')
    for i in range(len(count)):
        his = "*" * count[i]
        print(f'{his}')"""


def imageThreshing(): 
    gw =GWindow(600,400)
    image = GImage("Moon.png", 0,0)
    image.scale(gw.get_width()/image.get_width())
    gw.add(image)

    def imagetreshold(e):
        TRESHOLD = 130
        pixel = image.get_pixel_array()
        #print(pixel)
        for r in range(len(pixel)):
            for c in range(len(pixel[0])):
                value = pixel[r][c]
                red =GImage.get_red(value)
                if red< TRESHOLD:
                    pixel[r][c]= GImage.create_rgb_pixel(0,0,0)
                else:
                    pixel[r][c] = GImage.create_rgb_pixel(10, 0,255,0)
        # You must create a new Gimage
        new_image = GImage(pixel)

        gw.add(new_image)

    gw.add_event_listener("click", imagetreshold)

from math import sin, pi

def sine_file(filename, A, T, symbol, padding=" "):
    """ 
    Creates a new sine wave in the provided file with the provided amplitude (A),
    and period (T) with the indicated symbol at the end.

    Inputs:
        filename (string): the name of the file to write the art to
        A (int): the amplitude of the wave in terms of number of characters
        T (int): the period of the wave in terms of number of lines
        symbol (string): the symbol to place to mark the wave
        padding (string): what character to pad the left side of the wave with

    Outputs:
        None
    """

    def compute_symb_placement(A, T, x):
        """Computes where the symbol should be placed."""
        value = A * sin(2 * pi / T * x) + A
        return int(value) # to integer character placement

    def construct_line(placement, symbol, padding):
        """Constructs the line with the necessary padding and symbol at the end."""
        return padding * placement + symbol

    with open(filename, 'w') as fh:
        for x in range(10 * T): # write 10 periods worth of lines
            v = compute_symb_placement(A, T, x)
            line = construct_line(v, symbol, padding)
            fh.write(line + '\n') # need the newline character at the end!
    


if __name__ == "__main__":
    #tabulate()
    sine_file('sine_test.txt', A=30, T=50, symbol='X')
