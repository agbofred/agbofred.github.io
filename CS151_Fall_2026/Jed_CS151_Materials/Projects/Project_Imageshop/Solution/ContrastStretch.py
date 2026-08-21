# File: ContrastStretch.py

"""
Library for taking care of image histogram stretching.
"""

from pgl import GImage, GWindow
from GrayscaleImage import createGrayscaleImage, luminance


def calc_image_hist(image):
    """
    Computes a histogram array of the luminance values
    in the given image.
    """
    array = image.getPixelArray()
    hist = [0] * 256
    for row in array:
        for pixel in row:
            L = luminance(pixel)
            hist[L] += 1
    return hist

def create_hist_img(image, cumulative=False):
    """
    Creates a plot of the histogram array with the same
    dimensions as the original image.
    """
    counts = calc_image_hist(image)
    if cumulative:
        counts = calc_cum_hist(counts)
    xscale = 2
    W = 256 * xscale
    new_counts = []
    for c in counts:
        new_counts.extend(xscale*[c])
    counts = new_counts
    H = int(W/(4/3))
    max_v = max(counts)
    yscale = max_v / H
    c_img = [ [ GImage.create_rgb_pixel(255,255,255) for i in range(W)] for j in range(H)]
    for r in range(H):
        for c in range(W):
            if r > H - (counts[c]) // yscale:
                c_img[r][c] = GImage.create_rgb_pixel(0,0,0)
            if r==0 or r == H-1 or c == 0 or c == W-1:
                c_img[r][c] = GImage.create_rgb_pixel(0,0,0)

    return GImage(c_img)



def calc_cum_hist(hist):
    """
    Computes the cumulative histogram given an
    existing histogram array.
    """
    cumhist = [hist[0]] * len(hist)
    for i in range(1, len(hist)):
        cumhist[i] = cumhist[i - 1] + hist[i]
    return cumhist


def stretch_contrast(image):
    hist = calc_image_hist(image)
    chist = calc_cum_hist(hist)
    array = image.getPixelArray()
    total_pixels = len(array) * len(array[0])
    for i, row in enumerate(array):
        for j, pixel in enumerate(row):
            L = luminance(pixel)
            gray = round(255 * chist[L] / total_pixels)
            array[i][j] = GImage.createRGBPixel(gray, gray, gray)
    return GImage(array)


if __name__ == "__main__":
    gw = GWindow(800, 800)
    image = GImage("images/EarthFromApollo17.png")
    gw.add(
        createGrayscaleImage(image),
        gw.getWidth() / 2 - image.getWidth(),
        gw.getHeight() / 2 - image.getHeight() / 2,
    )
    stretched = stretch_contrast(image)
    gw.add(
        stretched, gw.getWidth() / 2, gw.getHeight() / 2 - stretched.getHeight() / 2,
    )
    print("Done")

