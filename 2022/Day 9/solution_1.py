def is_adjacent(head_position, tail_position):
    return abs(head_position[0] - tail_position[0]) <= 1 and abs(head_position[1] - tail_position[1]) <= 1

def move_in_direction(head_position, direction):
    if direction == "R":
        head_position = (head_position[0] + 1, head_position[1])
    elif direction == "L":
        head_position = (head_position[0] - 1, head_position[1])
    elif direction == "U":
        head_position = (head_position[0], head_position[1] + 1)
    elif direction == "D":
        head_position = (head_position[0], head_position[1] - 1)
    return head_position

def move_after_head(head_position, tail_position):
    if not is_adjacent(head_position, tail_position):
        if head_position[0] != tail_position[0]:
            left_right_update = 1 if head_position[0] > tail_position[0] else -1
        else:
            left_right_update = 0
        if head_position[1] != tail_position[1]:
            up_down_update = 1 if head_position[1] > tail_position[1] else -1
        else:
            up_down_update = 0
        tail_position = (tail_position[0] + left_right_update, tail_position[1] + up_down_update)
    return tail_position

def move(head_position, tail_position, direction):
    head_position = move_in_direction(head_position, direction)
    tail_position = move_after_head(head_position, tail_position)
    return (head_position, tail_position)

def solution(path):
    with open(path) as f:
        data = f.readlines()
    head_position = (0, 0)
    tail_position = (0, 0)
    tail_positions = {tail_position}
    for instruction in data:
        (direction, times) = instruction.split(' ')
        for _ in range(int(times)):
            head_position, tail_position = move(head_position, tail_position, direction)
            tail_positions.add(tail_position)
    return len(tail_positions)

if __name__ == "__main__":
    print(solution('example_input.txt'))
    print(solution('input.txt'))