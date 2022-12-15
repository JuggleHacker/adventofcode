def solution(path):
    with open(path) as f:
        data = f.readlines()
        rock_lines = parse_data_as_coordinates(data)
        blocked = blocked_locations(rock_lines)
        deepest_rock = max([coordinate[1] for coordinate in blocked])
        dropped = 0
        while True:
            next_sand_location = dropped_sand_final_location(blocked, deepest_rock)
            if next_sand_location == 'DONE':
                break
            else:
                blocked.add(next_sand_location)
                dropped += 1
        return dropped

def dropped_sand_final_location(blocked, deepest):
    sand_position = (500, 0)
    while True:
        if sand_position[1] > deepest:
            return 'DONE'
        down = (sand_position[0], sand_position[1]+1)
        if down not in blocked:
            sand_position = down
            continue
        down_left = (sand_position[0]-1, sand_position[1]+1)
        if down_left not in blocked:
            sand_position = down_left
            continue
        down_right = (sand_position[0]+1, sand_position[1]+1)
        if down_right not in blocked:
            sand_position = down_right
            continue
        else:
            return sand_position



def blocked_locations(rock_lines):
    blocked = set()
    for line in rock_lines:
        for i in range(len(line) - 1):
            start_x, start_y = line[i]
            end_x, end_y = line[i + 1]
            if start_x == end_x:
                step = 1 if start_y < end_y else -1
                while start_y != end_y:
                    blocked.add((start_x, start_y))
                    start_y += step
                blocked.add((start_x, start_y))
            else:
                step = 1 if start_x < end_x else -1
                while start_x != end_x:
                    blocked.add((start_x, start_y))
                    start_x += step
                blocked.add((start_x, start_y))
    return blocked


def parse_data_as_coordinates(data):
    parsed_lines = []
    for line in data:
        coords = [x.split(',') for x in line.split(' -> ')]
        for i, pair in enumerate(coords):
            x, y = pair
            coords[i] = (int(x), int(y))
        parsed_lines.append(coords)
    return parsed_lines



print(solution('example_input.txt'))
print(solution('input.txt'))