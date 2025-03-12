from pgl import GWindow, GImage, GLabel

def display_image():
    gw = GWindow(500,500)
    image= GImage("../images/Moon.png")
    image.scale(gw.get_width()/image.get_width())
    gw.add(image)
    
    caption = GLabel("This is a MOONSET images from NASA.ORG")
    caption.set_font("15px 'cosiva'")
    gw.add(caption, 30, image.get_height()+15)

    
    def threshholding(e):
        TH=120
        pixel = image.get_pixel_array()
        for i in range(len(pixel)):
            for j in range(len(pixel[0])):
                apixel = pixel[i][j]
                color_red = image.get_red(apixel)
                if color_red<TH:
                    pixel[i][j] = GImage.create_rgb_pixel(0,0,0)
                else:
                    pixel[i][j] = GImage.create_rgb_pixel(255,255,255)
        new_image= GImage(pixel)
        gw.add(new_image)
    gw.add_event_listener("click", threshholding)
    
display_image()