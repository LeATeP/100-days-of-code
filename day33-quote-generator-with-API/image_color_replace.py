import os, sys
from PIL import Image

# Detect pixel color in RGB
im = Image.open("./back2.png")
x = 100
y = 100

pix = im.load()[x, y]
r, g, b = pix[0], pix[1], pix[2]
# (251, 213, 58, 255)


# Replace pixel colors in image

OLD_PATH = im
NEW_PATH = r'back3.png'

R_OLD, G_OLD, B_OLD = (r, g, b)
R_NEW, G_NEW, B_NEW = (255, 0, 0)
# use the below site for getting RGB values of a given color in image
# https://imagecolorpicker.com/en
# R_NEW, G_NEW, B_NEW = (0, 174, 239) CYAN

im = Image.open(OLD_PATH)
pixels = im.load()

width, height = im.size
for x in range(width):
    for y in range(height):
        r, g, b, a = pixels[x, y]
        if (r, g, b) == (R_OLD, G_OLD, B_OLD):
            pixels[x, y] = (R_NEW, G_NEW, B_NEW, a)
im.save(NEW_PATH)
