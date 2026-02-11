from PIL import Image
import numpy as np

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