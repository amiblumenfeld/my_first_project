import os
print("Current folder:", os.getcwd())

from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display

# open the names file
file = open("greating_card/name_file.txt", "r")
names = file.readlines()
file.close()

count = 1
for name in names:
    name = name.strip()

    # background
    img = Image.new("RGB", (800, 400), color="lightblue")
    draw = ImageDraw.Draw(img)

    # text
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", 60)

    # first line:
    line1 = "חג שמח"
    bbox1 = draw.textbbox((0, 0), line1, font=font)
    w1 = bbox1[2] - bbox1[0]
    x1 = (img.width - w1) / 2
    y1 = (img.height / 2) - 80
    draw.text((x1, y1), line1, fill="darkblue", font=font)

    # second line:
    line2 = "ל" + name
    bbox2 = draw.textbbox((0, 0), line2, font=font)
    w2 = bbox2[2] - bbox2[0]
    x2 = (img.width - w2) / 2
    y2 = y1 + 100
    draw.text((x2, y2), line2, fill="darkblue", font=font)

    # add flowers
    flower = Image.open("flower.png").resize((200, 200))
    img.paste(flower, (600, 10), flower)

    flower2 = Image.open("flower2.png").resize((250, 250))
    img.paste(flower2, (15, 140), flower2)

    # save card
    img.save("holiday_card" + str(count) + ".png")
    count = count + 1