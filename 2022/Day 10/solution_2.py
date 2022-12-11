def draw(pixels):
    screen = [['.'] * 40 for _ in range(6)]
    for row_number in range(6):
        for column in range(40):
            if row_number * 40 + column + 1 in pixels:
                screen[row_number][column] = '#'
    return screen

def draw_hash(cycle, x):
    print(f"Cycle: {cycle} x: {x}")
    y = cycle % 40 - 1
    return abs(y - x) <= 1

def solution(path):
    with open(path) as f:
        instructions = f.readlines()
    x = 1
    cycle = 0
    next_instruction_number = 0
    pixels = set()
    while True:
        instruction = instructions[next_instruction_number]
        next_instruction_number += 1
        if next_instruction_number == len(instructions):
        # if next_instruction_number == 20:
            break
        if instruction[:4] == 'noop':
            cycle += 1
            if draw_hash(cycle, x):
                pixels.add(cycle)
        elif instruction[:4] == 'addx':
            to_add = int(instruction[5:])
            print(to_add)
            cycle += 1
            if draw_hash(cycle, x):
                pixels.add(cycle)
            cycle += 1
            if draw_hash(cycle, x):
                pixels.add(cycle)
            x += to_add

    print(pixels)
    for row in draw(pixels):
        print(''.join(row))


# print(solution('example_input.txt'))
print(solution('input.txt'))