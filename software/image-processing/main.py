from imagetools import preview_image, convert_image_to_RGB, resize
from greyscale import convert_RGB_to_luminosity_greyscale
from gaussian import gaussian_blur
from edge_detection import sobel_edge_detection
from greyscalethreshold import greyscale_threshold


print("Image converting to RGB")
rgb_image = convert_image_to_RGB("/Users/ewanmccairn/Downloads/theloq.png")
print("Done!")
print("Resizing image...")
resized_image = resize(rgb_image, 500, 500)
print("Done!")
print("Image converting to greyscale...")
image_array = convert_RGB_to_luminosity_greyscale(rgb_image)
print("Done!")

print("Blurring image...")
blurred_array = gaussian_blur(image_array, 0.75)
print("Done!")

print("Applying Sobel operator...")
sobel_array = sobel_edge_detection(blurred_array)
print("Done!")

print("Thresholding...")
thresholded_array = greyscale_threshold(sobel_array, 50) # chosen threshold 50/255
print("Done!")

print("Previewing...")
preview_image(resized_image)