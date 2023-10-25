from pgl import GImage, GWindow, GLabel

def image_example():
    gw = GWindow(800, 550)
    image = GImage("VLA_Moonset.jpg")
    #image.scale(gw.get_width() / image.get_width())
    gw.add(image)
    print(image.get_pixel_array())

    citation = GLabel("Image Credit: Jeff Hellermann, NRAO / AUI / NSF")
    citation.set_font("15px 'Sans-Serif'")
    x = gw.get_width() - citation.get_width() - 10
    y = image.get_height() + citation.get_ascent()
    gw.add(citation, x, y)

image_example()
