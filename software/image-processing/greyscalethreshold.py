def greyscale_threshold(image, threshold_value):
    new_threshold_image = []
    for row in image:
        new_threshold_row = []
        for pixel in row:
            if pixel[0] > threshold_value:
                new_threshold_row.append([255, 255, 255])
            else:
                new_threshold_row.append([0, 0, 0])
        new_threshold_image.append(new_threshold_row)
    return new_threshold_image