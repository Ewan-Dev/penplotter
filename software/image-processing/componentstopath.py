def get_neighbours(pixel, component):
    x,y = pixel
    neighbours=[]
    for x_diff in [-1,0,1]:
        for y_diff in [-1,0,1]:
            if x_diff ==0 and y_diff == 0:
                continue
            if (x+x_diff, y+y_diff) in component:
                neighbours.append(((x+x_diff, y+y_diff)))
    return neighbours

def find_start(component):
    pixels_set = set(component)

    for pixel in component:
        if len(get_neighbours(pixel, pixels_set)) == 1:
            return pixel
    
    return component[0]


components = [[(0,1),(0,3),(0,6),(0,2), (0,5),(0,4)], [(0,9),(0,10),(0,11),(0,12), (0,14),(0,13)]]
for i in range(len(components)):
    start = find_start(components[i])
    visited = set()
    current_pixel = start
    visited.add(current_pixel)
    ordered_pixels = [current_pixel]
    while True:
        neigbours = []
        for pixel in get_neighbours(current_pixel, set(components[i])):
            if pixel not in visited:
                neigbours.append(pixel)
        if not neigbours:
            break
        next_pixel = neigbours[0]
        visited.add(next_pixel)
        current_pixel = next_pixel
        ordered_pixels.append(next_pixel)

        
    print(ordered_pixels)
