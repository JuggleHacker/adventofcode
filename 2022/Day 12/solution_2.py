def is_reachable(start_height, end_height):
    heights = 'SabcdefghijklmnopqrstuvwxyzE'
    return heights.index(end_height) - 1 <= heights.index(start_height)

def next_reachable(current_reachable, grid):
    next_reachable = set()
    rows = len(grid)
    cols = len(grid[0])
    for (x, y) in current_reachable:
        current_height = grid[y][x]
        if x + 1 < cols:
            new_height = grid[y][x+1]
            if is_reachable(current_height, new_height):
                next_reachable.add((x+1, y))
        if x - 1 >= 0:
            new_height = grid[y][x-1]
            if is_reachable(current_height, new_height):
                next_reachable.add((x-1, y))
        if y + 1 < rows:
            new_height = grid[y+1][x]
            if is_reachable(current_height, new_height):
                next_reachable.add((x, y+1))
        if y - 1 >= 0:
            new_height = grid[y-1][x]
            if is_reachable(current_height, new_height):
                next_reachable.add((x, y-1))
    return next_reachable


def solution(path):
    with open(path) as f:
        data = f.readlines()
        grid = [line.strip() for line in data]
        reachable = {(line.index('a'), line_number) for line_number, line in enumerate(grid) if 'a' in line}
        target = [(line.index('E'), line_number) for line_number, line in enumerate(grid) if 'E' in line][0]
        visited = set()
        steps = 0
        while target not in reachable:
            steps += 1
            visited = visited.union(reachable)
            reachable = {place for place in next_reachable(reachable, grid) if place not in visited}
        print(steps)

# print(solution('example_input.txt'))
print(solution('input.txt'))