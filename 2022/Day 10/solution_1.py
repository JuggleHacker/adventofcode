def value_of_x_after_n_cycle(instructions, n):
    x = 1
    cycles = 0
    next_instruction_number = 0
    while cycles < n:
        instruction = instructions[next_instruction_number]
        next_instruction_number += 1
        if instruction[:4] == 'noop':
            cycles += 1
        elif instruction[:4] == 'addx':
            to_add = int(instruction[5:])
            cycles += 2
            if cycles < n:
                x += to_add
    return x

def solution(path):
    with open(path) as f:
        data = f.readlines()
    sum_of_signals = 0
    for n in range(20,300, 40):
    # for n in [20]:
        signal_strength = n * value_of_x_after_n_cycle(data, n)
        print(f"{n} : {signal_strength}")
        sum_of_signals += signal_strength
        print(sum_of_signals)

# print(solution('example_input.txt'))
print(solution('input.txt'))