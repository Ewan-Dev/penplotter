def get_components(image_array):
    height = len(image_array)
    width = len(image_array[0])

    visited = [[False for i in range(width)] for i in range(height)] #each pixel starts off as not visited
    components = []

    def flood_fill(x0, y0):
        stack = [(x0, y0)] #pop pixel, add its neighbours. repeat until stack is empty
        component = []
        while stack:
            x, y = stack.pop()
            if x < 0 or y < 0 or x >= width or y >= height:
                continue
            if visited[y][x]:
                continue
            if image_array[y][x] == 0:
                continue

            visited[y][x] = True
            component.append((x, y))

            neighbors = [
                (1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1)
            ]
            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx] and image_array[ny][nx] == 1:
                    stack.append((nx, ny)) #if neighbours pass all checks (inside image, not white) then add to stack to be processed later
        return component

    for y in range(height):
        for x in range(width):
            if image_array[y][x] == 1 and not visited[y][x]:
                component = flood_fill(x,y)
                components.append(component)
    
    return components