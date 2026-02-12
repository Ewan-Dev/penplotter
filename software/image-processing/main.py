from imagetools import preview_image, convert_image_to_RGB, gaussian_blur, gaussian_kernel
from greyscale import convert_RGB_to_luminosity_greyscale
image_array = convert_RGB_to_luminosity_greyscale(convert_image_to_RGB('/Users/ewanmccairn/Downloads/AI Animals Brainrot.jpeg'))
preview_image(gaussian_blur(image_array, 20))
