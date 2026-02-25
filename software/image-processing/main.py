from imagetools import preview_image, convert_image_to_RGB, resize
from greyscale import convert_RGB_to_luminosity_greyscale
from gaussian import gaussian_blur
from edge_detection import sobel_edge_detection
from greyscalethreshold import greyscale_threshold
from zhangseunthinning import zhang_suen_thinning


print("Image converting to RGB")
rgb_image = convert_image_to_RGB("images/python.png")
preview_image(rgb_image)
print("Done!")
print("Resizing image...")
resized_image = resize(rgb_image, 500, 500)
preview_image(resized_image)
print("Done!")
print("Image converting to greyscale...")
image_array = convert_RGB_to_luminosity_greyscale(resized_image)
preview_image(image_array)
print("Done!")

print("Blurring image...")
blurred_array = gaussian_blur(image_array, 0.75)
preview_image(blurred_array)
print("Done!")

print("Applying Sobel operator...")
sobel_array = sobel_edge_detection(blurred_array)
preview_image(sobel_array)
print("Done!")

print("Thresholding...")
thresholded_array = greyscale_threshold(sobel_array, 150) # chosen threshold 50/255
preview_image(thresholded_array)
print("Done!")

print("Zhang-Suen thinning")
thinned_image = zhang_suen_thinning(thresholded_array)
preview_image(thresholded_array)
print("Done!")

print("Previewing...")
preview_image(thinned_image)