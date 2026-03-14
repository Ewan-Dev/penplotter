def rgb_to_binary(image_array):
    binary = []
    for row in image_array:
        new_row = []
        for pixel in row:
            if isinstance(pixel, (tuple, list)) and len(pixel) >= 3:
                # binary foreground is black
                new_row.append(1 if pixel[0] < 128 and pixel[1] < 128 and pixel[2] < 128 else 0)
            elif isinstance(pixel, (tuple, list)) and len(pixel) == 1:
                new_row.append(1 if pixel[0] != 0 else 0)
            elif isinstance(pixel, int):
                new_row.append(1 if pixel != 0 else 0)
            else:
                try:
                    new_row.append(1 if float(pixel) != 0.0 else 0)
                except Exception:
                    new_row.append(0)
        binary.append(new_row)
    return binary
