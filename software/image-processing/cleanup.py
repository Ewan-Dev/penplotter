def clean_image(image_array, clean_iterations):
    current_image = image_array
    for i in range(int(clean_iterations)):
        cleaned_array = []
        image_width = len(current_image[0])
        image_height = len(current_image)
        for y in range(1, image_height-1):
            cleaned_row = []
            for x in range(1, image_width-1):
                if x == 0 or y == 0 or x == image_width-1 or y == image_height-1:
                    cleaned_row.append(current_image[y][x])
                    continue
                kernel = [[current_image[y-1][x-1],current_image[y-1][x],current_image[y-1][x+1]],
                        [current_image[y][x-1],current_image[y][x],current_image[y][x+1]],
                        [current_image[y+1][x-1],current_image[y+1][x],current_image[y+1][x+1]]]
                if clean(kernel) == 1:
                    cleaned_row.append((255,255,255))
                else:
                    cleaned_row.append(current_image[y][x])
            cleaned_array.append(cleaned_row)
        current_image = cleaned_array
    return cleaned_array


def clean(kernel):
    neighbours = 0
    for y in range(3):
        for x in range(3):
            if (y != 1 or x != 1) and kernel[y][x] == (0, 0, 0):
                neighbours += 1
    if neighbours < 2:
        return 1
    else:
        return 0
