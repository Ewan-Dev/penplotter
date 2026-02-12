from PIL import Image
import numpy as np
import math

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

def gaussian_blur(image_array, strength):
    new_image_array = []
    size =  (2 * math.ceil(3 * strength) + 1) 
    height = len(image_array)
    width = len(image_array[0])
    kernel = gaussian_kernel(strength)
    for y in range(height):
        new_image_row = []
        for x in range(width):
            new_r = 0
            new_g = 0
            new_b = 0
            for kernel_x in range(size):
                for kernel_y in range(size):
                    relative_kernel_pixel_x = kernel_x - (size // 2)
                    relative_kernel_pixel_y = kernel_y - (size // 2)
                    # surrounding pixels from kernel size timed by kernel weights weight
                    current_x = x + relative_kernel_pixel_x
                    current_y = y + relative_kernel_pixel_y
                    if 0 <= current_x < width and 0 <= current_y < height:
                        r, g, b = image_array[current_y][current_x]
                        weighting = kernel[kernel_y][kernel_x]
                        new_r += r * weighting
                        new_g += g * weighting
                        new_b += b * weighting
            new_pixel = (new_r, new_g, new_b)
            new_image_row.append(new_pixel)
        new_image_array.append(new_image_row)
    return new_image_array

def gaussian_formula(x, y, sigma):
    return math.e**(-(x**2 + y**2)/(2*(sigma)**2))


def gaussian_kernel(strength):
    size =  2 * math.ceil(3 * strength) + 1
    x_coords = [] # x co-ords
    y_coords = [] # y co-ords
    weight_total = 0
    max_val = int(size // 2)
    # lays out possible x and y co-ords
    for i in range(-max_val, max_val + 1):
        x_coords.append(i)
        y_coords.append(i)

    kernel_weights = []
    for y in y_coords:
        row_weights = []
        for x in x_coords:
            weight = gaussian_formula(x, y, strength)
            row_weights.append(weight)
            weight_total += weight
        kernel_weights.append(row_weights)

    for y in range(size):
        for x in range(size):
            kernel_weights[y][x] /= weight_total
            kernel_weights[y][x] = round(kernel_weights[y][x], 5)

    return kernel_weights

