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