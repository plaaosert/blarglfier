import colorsys
import math
import os
import random

from PIL import Image


def blarglify_image(img: Image.Image) -> Image.Image:
    out_img = img.resize((64, 64), Image.NEAREST)

    hueshift = random.randint(0, 359) / 360

    w, h = out_img.size
    for x in range(w):
        for y in range(h):
            hsv = colorsys.rgb_to_hsv(*out_img.getpixel((x, y)))
            new_hsv = (((hsv[0] + hueshift) % 1), *hsv[1:])
            new_rgb = tuple(int(t) for t in colorsys.hsv_to_rgb(*new_hsv))
            out_img.putpixel((x, y), new_rgb)

    level = 100
    factor = (259 * (level + 255)) / (255 * (259 - level))

    def contrast(c):
        return 128 + factor * (c - 128)

    out_img = out_img.point(contrast)

    out_img = out_img.resize((250, 250), Image.NEAREST)

    w, h = out_img.size
    for x in range(w):
        for y in range(h):
            brightness = math.sin(y)
            brightness *= 0.1

            old_rgb = out_img.getpixel((x, y))

            new_rgb = tuple(min(255, max(0, old_rgb[i] - int(255 * brightness))) for i in range(3))

            out_img.putpixel((x, y), new_rgb)

    return out_img


for image in os.listdir("imgs"):
    path = os.path.join("imgs", image)

    img_original: Image.Image = Image.open(path)
    blarglified_image: Image.Image = blarglify_image(img_original)

    blarglified_image.save(os.path.join("output", image))
