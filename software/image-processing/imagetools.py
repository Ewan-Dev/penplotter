from PIL import Image
import numpy as np
import math

    # using nearest neighbour resizing as later image processing makes interpolation negligible
def resize(image, new_width, new_height):
    old_height = len(image)
    old_width= len(image[0])

    # handles cases where not all sizing parameters are inputted
    if new_width and not new_height:
        aspect_ratio = old_width/old_height
        new_height = int(new_width / aspect_ratio)
    elif new_height and not new_width:
        aspect_ratio = old_width/old_height
        new_width = int(new_height * aspect_ratio)
    elif not new_width and not new_height:
        raise Exception("You need at least one sizing parameter")
    

    new_image = [[0 for _ in range(new_width)] for _ in range(new_height)] # 2d array for resized array

    for y in range(new_height):
        for x in range(new_width):
            # scale factor * coordinate = new coordinate
            new_x = int(x * (old_width/new_width))
            new_y = int(y * (old_height/new_height))
            new_image[y][x] = image[new_y][new_x]
    return new_image

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