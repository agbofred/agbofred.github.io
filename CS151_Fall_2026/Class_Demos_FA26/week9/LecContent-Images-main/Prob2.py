from pgl import GWindow, GImage, GRect

GW_WIDTH = 900
GW_HEIGHT = 650

gw = GWindow(GW_WIDTH, GW_HEIGHT)

rect = GRect(0,0,GW_WIDTH, GW_HEIGHT)
rect.set_fill_color("darkblue")
rect.set_filled(True)
gw.add(rect)

image = GImage("Moon.png")
gw.add(image, GW_WIDTH/2 - image.get_width()/2, GW_HEIGHT/2 - image.get_height()/2)

"""
pixel_array= image.get_pixel_array()

heigth = len(pixel_array)
width = len(pixel_array[0])
count =0
for r in range(heigth):
    for c in range(width):
        pixel = pixel_array[r][c]
        brightness = GImage.get_red(pixel)
        if brightness < 100:
            # count +=1
            pixel_array[r][c] = GImage.create_rgb_pixel(0,0,0)
        else:
            pixel_array[r][c] = GImage.create_rgb_pixel(255,100,255)
new_image = GImage(pixel_array)
gw.add(new_image, image.get_x(), image.get_y()) 
"""

