from imagetools import preview_image, convert_image_to_RGB
from greyscale import convert_RGB_to_luminosity_greyscale
from gaussian import gaussian_blur
from edge_detection import sobel_edge_detection

image_array = convert_RGB_to_luminosity_greyscale(convert_image_to_RGB('C:\\Users\\maxkp\\CrossDevice\\Pixel 7a\\storage\\Pictures\\Screenshots\\Screenshot_20260131-212000.png'))
blurred_array = gaussian_blur(image_array, 0.75)
edges_array = sobel_edge_detection(blurred_array)

edges_preview = []

max_val = max(max(row) for row in edges_array)
edges_normalised = []

for row in edges_array: #cap and normalise magnitudes at 255 so uint8 can handle them
    new_row = []  
    for magnitude in row: 
        
        normalised_value = (magnitude / max_val) * 255
        normalised_value = round(normalised_value)  
        new_row.append(normalised_value)  
    edges_normalised.append(new_row)  


for row in edges_normalised: #edges preview e.g [170, 170] becomes [(170,170,170), (170,170,170)]
    new_row = []
    for magnitude in row:
        new_row.append((magnitude, magnitude, magnitude))
    edges_preview.append(new_row)

preview_image(edges_preview)