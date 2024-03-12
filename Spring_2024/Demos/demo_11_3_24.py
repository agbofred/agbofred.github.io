from pgl import GWindow, GImage

def imagethreshold():
    gw = GWindow(800,550)
    image = GImage("Moon.png",0,0)
    image.scale(gw.get_width()/ image.get_width())
    gw.add(image)
    def threshold(e):
        THRESHOLD = 130
        pixel = image.get_pixel_array()
        print(pixel)
        for r in range(len(pixel)):
            for c in range(len(pixel[0])):
                value = pixel[r][c]
                red = GImage.get_red(value)
                if red < THRESHOLD:
                    pixel[r][c] = GImage.create_rgb_pixel(0,0,0)
                else:
                    pixel[r][c] = GImage.create_rgb_pixel(255,255,255)
        new_image = GImage(pixel)
        gw.add(new_image)
    gw.add_event_listener("click", threshold)



if __name__ == "__main__":
    imagethreshold()
    pass

#########################
# File chooser 
###########################

from filechooser import choose_input_file, choose_output_file
from pgl import GWindow, GImage



def finput():
    filen = choose_input_file()
    gw = GWindow(800, 500)
    img = GImage(filen, 0,0)
    img.scale(gw.get_width()/(img.get_width()*2))
    gw.add(img)
#finput() 





#########################
# Writing file to text
######################

""" days =["Raining Sunday"]
week = ["Week 1", "Week 2"]

with open ("cs151_10.txt", "w") as fh:
    for i in range(len(days)):
        fh.write(days[i])
 """

def foutput():
    filename= choose_output_file()
    if filename=="":
        print("no File name! Cancled")
    else:
        days =["Sunday", "Monday", "Teusdays", "Wednesday", "Thursday", "Friday", "Saturday", "Restday", "Godbye"]
        month =["Jan", "Feb"]
        with open(filename, "w") as fh:
            for k in range(len(days)):
                fh.write(month[k]+"\n")
#foutput()



############################
# Writing a Sin Wave
#############################

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

if __name__ == '__main__':
    #sine_file('sine_test.txt', A=10, T=20, symbol='x')
    pass

