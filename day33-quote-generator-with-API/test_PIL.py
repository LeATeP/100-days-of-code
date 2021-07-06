import sys
from PIL import Image, ImageDraw, ImageFont
import textwrap, random, os, pandas as pd, numpy as np, cv2 as cv, requests
import text2emotion as te, operator

# https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil

# Create Image object
im = Image.open("./back2.png")

# bg changing
pixel_position_x, pixel_position_y = 100, 100

pix = im.load()[pixel_position_x, pixel_position_y]
r, g, b = pix[0], pix[1], pix[2]
r2, g2, b2 = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
R_OLD, G_OLD, B_OLD = (r, g, b)
R_NEW, G_NEW, B_NEW = (r2, g2, b2)

pixels = im.load()
width, height = im.size
for x in range(width):
    for y in range(height):
        r, g, b, a = pixels[x, y]
        if (r, g, b) == (R_OLD, G_OLD, B_OLD):
            pixels[x, y] = (R_NEW, G_NEW, B_NEW, a)


# loading quote
data = requests.get(url="https://type.fit/api/quotes")
data.raise_for_status()
quotes = data.json()
file = random.choice(quotes)
text = file["text"]
author = file["author"]


#  Determine Emotion
get_emotion = te.get_emotion(text)
emotion = max(get_emotion.items(), key=operator.itemgetter(1))[0]
if get_emotion[emotion] == 0:
    emotion = "Happy"


# random Emoji
folder_emotion = f"./Emoji/{emotion}"
emoji = random.choice([x for x in os.listdir(f"{folder_emotion}")
                       if os.path.isfile(os.path.join(f"{folder_emotion}", x))])
im2 = Image.open(f"{folder_emotion}/{emoji}")

Image1copy = im.copy()
Image2copy = im2.copy()

# Draw line
# draw = ImageDraw.Draw(Image1copy)
# draw.line((0, 0) + Image1copy.size, fill=128)
# draw.line((0, Image1copy.size[1], Image1copy.size[0], 0), fill=128)

bg_w, bg_h = im.size

draw = ImageDraw.Draw(Image1copy)

# specified font size


# 200 text = 'Translation is the paradigm, the exemplar of all writing.
# It is translation that demonstrates most vividly the yearning
# for transformation that underlies every act involving speech, that supremely human gift.'

# 50 text = "Nothing strengthens authority so much as silence."

font_size = 25
if len(text) > 100:
    font_size = 20

font = ImageFont.truetype(r'arial.ttf', font_size)

length = len(text)
para = textwrap.wrap(text, width=28)
x = (-0.6137 * length) + 183.63
print(x)
current_h, pad = x, 10

MAX_W, MAX_H = 325, 400
# drawing text size
# draw.text((5, 35), text, font = font, align ="left")
for line in para:
    w, h = draw.textsize(line, font=font)
    print(w, h)
    draw.text(((MAX_W - w) / 2, current_h), line, font=font, fill="black")
    current_h += h + pad

Image1copy.paste(Image2copy, (120, 310), Image2copy)
# Image1copy.paste(Image1copy, (bg_w, bg_h), Image1copy)

Image1copy.save(f"my_drawing{random.randint(0, 5000)}.png")

# Show image
Image1copy.show()
