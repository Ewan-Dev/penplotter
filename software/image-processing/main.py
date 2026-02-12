from imagetools import preview_image, convert_image_to_RGB
from greyscale import convert_RGB_to_luminosity_greyscale
from gaussian import gaussian_blur

image_array = convert_RGB_to_luminosity_greyscale(convert_image_to_RGB('/Users/ewanmccairn/Downloads/AI Animals Brainrot.jpeg'))
preview_image(gaussian_blur(image_array, 0.75))
