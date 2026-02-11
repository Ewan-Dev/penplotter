from PIL import Image
import numpy as np
from math import pi, exp

def convert_image_to_RGB(path):
    img = Image.open(path)
    img_RGB = img.convert("RGB")
    width, height = img.size

    img_array = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = img_RGB.getpixel((x, y))
            row.append(pixel)
        img_array.append(row)
    return img_array

def preview_image(image_array):
    img = Image.fromarray(np.array(image_array, dtype=np.uint8)) #uint8 for unisgned integer /0-255
    img.show()


#strength = input()  (odd)

def gaussian_blur(greyscale_array, strength):
    kernel_size = 2 * int(3 * strength) + 1
    kernel = gaussian_kernel(kernel_size, strength)

def gaussian_kernel(size, strength):
    kernel = []
    center = size // 2

    weight_total = 0 #keep cap under 1 later

    for row in range(size):
        row_weighting = []
        for columm in range(size):
            x = row - center #distances from centre to adjust weighting
            y = column - center

            weight = (1 / (2 * pi * strength ** 2)) * exp(-(x ** 2 + y ** 2) / (2 * strength ** 2)) #formula

            row_weighting.append(weight)
            weight_total += 1

    kernel.append(weight_total)


            
