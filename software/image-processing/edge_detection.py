import math

sobel_x = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

sobel_y = [
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
]

def sobel_edge_detection(greyscale_img_array):
    edge_array = []
    height = len(greyscale_img_array) 
    width = len(greyscale_img_array[0])

    for y in range(1, height-1):   #ignore edges
        new_row = []
        for x in range(1, width-1): 
            
            patch = []
            for dy in range(-1, 2):  #create 3x3 patch
                row = []
                for dx in range(-1, 2):
                    pixel_value = greyscale_img_array[y + dy][x + dx][0]
                    row.append(pixel_value)
                patch.append(row)
            Gx = 0
            Gy = 0
            for ky in range(3):
                for kx in range(3):
                    Gx += patch[ky][kx] * sobel_x[ky][kx] #multiply each patch value by corresponding sobel value
                    Gy += patch[ky][kx] * sobel_y[ky][kx]
            magnitude = round(math.sqrt(Gx**2 + Gy**2))

            new_row.append(magnitude)
        edge_array.append(new_row)

    return edge_array