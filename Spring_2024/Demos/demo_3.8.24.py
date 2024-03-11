from pgl import GImage, GWindow, GLabel
# Remeber to update the ANTIALIAS in PLG

def image_example():
    gw = GWindow(800, 550)
    image = GImage("/Users/fjagbo/Documents/GitHub/agbofred.github.io/Spring_2024/Demos/Moon.png")
    image.scale(gw.get_width() / image.get_width())
    gw.add(image)
    pixel=image.get_pixel_array()
    print(pixel[2][3])
    

    citation = GLabel("Image Credit: Jeff Hellermann, NRAO / AUI / NSF")
    citation.set_font("15px 'Sans-Serif'")
    x = gw.get_width() - citation.get_width() - 10
    y = image.get_height() + citation.get_ascent()
    gw.add(citation, x, y)

image_example()


"""with open("/Users/fjagbo/Documents/GitHub/agbofred.github.io/Spring_2024/Demos/demo_3.8.24.txt") as f:
    txt = f.read().splitlines()
    print(txt)
 for i in txt:
    if (len(i)>7):
        print(i)  """ 
    


""" pixel =[]
     for i in image.get_pixel_array():
        pixel.append(i)
    
    print(pixel[2][2]) 
    """