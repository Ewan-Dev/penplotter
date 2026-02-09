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

# using luminosity greyscale for better representation 
def convert_RGB_to_luminosity_greyscale(rgb_img_array):
    greyscale_img_array = []
    for row in rgb_img_array:
        new_row = []
        for pixel in row:
            red = pixel[0] * 0.21
            green = pixel[1] * 0.72
            blue = pixel[2] * 0.07
            new_pixel = red + green + blue
            new_row.append((new_pixel, new_pixel, new_pixel))
        greyscale_img_array.append(new_row)
    return greyscale_img_array

def preview_image(image_array):
    img = Image.fromarray(np.array(image_array, dtype=np.uint8)) #uint8 for unisgned integer /0-255
    img.show()

#preview_image(convert_RGB_to_luminosity_greyscale(convert_image_to_RGB('/Users/ewanmccairn/Downloads/AI Animals Brainrot.jpeg')))