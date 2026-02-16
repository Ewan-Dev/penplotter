from imagetools import preview_image, convert_image_to_RGB
from greyscale import convert_RGB_to_luminosity_greyscale
from gaussian import gaussian_blur
from edge_detection import sobel_edge_detection
from greyscalethreshold import greyscale_threshold

image_array = convert_RGB_to_luminosity_greyscale(convert_image_to_RGB("/Users/ewanmccairn/Downloads/Group 63 from Figma.png"))
blurred_array = gaussian_blur(image_array, 0.75)
sobel_array = sobel_edge_detection(blurred_array)
thresholded_array = greyscale_threshold(sobel_array, 50) # chosen threshold 50/255

preview_image(thresholded_array)