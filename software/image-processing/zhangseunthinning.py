def zhang_suen_thinning(image_array):
    image_array_binary= []
    new_image = []
    for y in range(len(image_array)):
        row = []
        # zhang seun expects '0' for foregound and '1' for  background
        for x in range(len(image_array[0])):
            if image_array[y][x][0] < 128 and image_array[y][x][1] < 128 and image_array[y][x][2] < 128:
                row.append(1)
            else:
                row.append(0)
        image_array_binary.append(row)
    while True:
            changed = False
            to_remove = [] # stores pixels marked for removal
            for y in range(1, len(image_array_binary) - 1):
                for x in range(1, len(image_array_binary[0]) - 1):
                    if image_array_binary[y][x] == 1:
                            neighbours = [
                                image_array_binary[y-1][x-1], image_array_binary[y-1][x], image_array_binary[y-1][x+1],
                                image_array_binary[y][x+1], image_array_binary[y+1][x+1], image_array_binary[y+1][x],
                                image_array_binary[y+1][x-1], image_array_binary[y][x-1]
                            ]
                            neighbour_count = sum(neighbours)
                            if neighbour_count < 2 or neighbour_count > 6:
                                continue
                            b_w_transitions = 0
                            for i in range (8):
                                if neighbours[i] == 0 and neighbours[(i+1) % 8] == 1:
                                    b_w_transitions += 1
                            if b_w_transitions != 1:
                                continue
                            if neighbours[1] * neighbours[3] * neighbours[5] != 0:
                                continue
                            if neighbours[3] * neighbours[5] * neighbours[7] != 0:
                                continue

                            to_remove.append((x, y))
            if to_remove:
                changed = True
                for x,y in to_remove:
                    image_array_binary[y][x] = 0

            to_remove = []
            for y in range(1, len(image_array_binary) - 1):
                for x in range(1, len(image_array_binary[0]) - 1):
                    if image_array_binary[y][x] == 1:
                            neighbours = [
                                image_array_binary[y-1][x-1], image_array_binary[y-1][x], image_array_binary[y-1][x+1],
                                image_array_binary[y][x+1], image_array_binary[y+1][x+1], image_array_binary[y+1][x],
                                image_array_binary[y+1][x-1], image_array_binary[y][x-1]
                            ]
                            neighbour_count = sum(neighbours)
                            if neighbour_count < 2 or neighbour_count > 6:
                                continue
                            b_w_transitions = 0
                            for i in range (8):
                                if neighbours[i] == 0 and neighbours[(i+1) % 8] == 1:
                                    b_w_transitions += 1
                            if b_w_transitions != 1:
                                continue
                            if neighbours[1] * neighbours[3] * neighbours[7] != 0:
                                continue
                            if neighbours[1] * neighbours[5] * neighbours[7] != 0:
                                continue
                            to_remove.append((x, y))
            if to_remove:
                changed = True
                for x,y in to_remove:
                    image_array_binary[y][x] = 0
            if not changed:
                break

    result = []
    for y in range(len(image_array_binary)):
        row = []
        for x in range(len(image_array_binary[0])):
            if image_array_binary[y][x] == 1:
                row.append((0, 0, 0))
            else:
                row.append((255, 255, 255))
        result.append(row)
    
    return result