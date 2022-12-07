def update_stacks_with_line(stacks, line):
    for index, character in enumerate(line):
        if character not in {' ', '[', ']', '\n'}:
            stacks_number = (index - 1) // 4
            stacks[stacks_number] = [character] + stacks[stacks_number]
    return stacks

def update_stacks_with_instruction(stacks, instruction):
    start, end = instruction.split(' from ')
    amount = int(start[5:])
    foo, bar = end.split(' to ')

    start_stack = int(foo) - 1
    end_stack = int(bar) - 1
    print(amount)
    print(start_stack)
    print(end_stack)
    print()
    moving = stacks[start_stack][-amount:][::-1]
    stacks[start_stack] = stacks[start_stack][:-amount]
    stacks[end_stack] += moving


# with open('example_input.txt') as f:
with open('input.txt') as f:
    line = f.readline()
    number_of_stacks = len(line) // 4
    stacks = [[] for _ in range(number_of_stacks)]
    while '1' not in line:
        stacks = update_stacks_with_line(stacks, line)
        line = f.readline()
    print(stacks)
    blank_line = f.readline()
    while True:
        instruction = f.readline()
        if instruction == '':
            break
        else:
            update_stacks_with_instruction(stacks, instruction)
        print(stacks)
    for stack in stacks:
        if len(stack) > 0:
            print(stack[-1], end='')
        else:
            print(' ')
