from pgl import GWindow, GImage

"""def imagethreshold():
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
"""


#if __name__ == "__main__":
    #imagethreshold()
"""from pgl import GWindow, GOval, GImage

gw =GWindow(600,400)
image = GImage("Moon.png", 0,0)
image.scale(gw.get_width()/image.get_width())
gw.add(image)
pixel = image.get_pixel_array()
print(pixel)

def threshold(event):
    THRESHOLD =100
    for r in range(len(pixel)):
        for c in range(len(pixel[0])):
            value = pixel[r][c]
            red = GImage.get_red(value)
            if red <THRESHOLD:
                pixel[r][c] = GImage.create_rgb_pixel(0,0,0) 
            else:
                pixel[r][c] = GImage.create_rgb_pixel(200,0,240,0) 
    newIm = GImage(pixel)
    gw.add(newIm)
gw.add_event_listener("click", threshold)
"""

with open("todaydemo.txt") as file:
    txt = file.read().splitlines()
    """text_l = txt.splitlines()
    for i in text_l:"""
for i in txt:
    nt = txt[1][:]
print(repr(nt))
    

