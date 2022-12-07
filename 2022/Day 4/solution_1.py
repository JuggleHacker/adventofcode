def fully_contains(a_min, a_max, b_min, b_max):
    a_contains_b = a_min <= b_min and b_max <= a_max
    b_contains_a = b_min <= a_min and a_max <= b_max
    return a_contains_b or b_contains_a

def parse_line(line):
    elf_a, elf_b = line.split(',')
    a_min, a_max = elf_a.split('-')
    b_min, b_max = elf_b.split('-')
    b_max = b_max[:-1] if b_max[-1] == '\n' else b_max
    return (int(a_min), int(a_max), int(b_min), int(b_max))

# with open('example_input.txt') as f:
with open('input.txt') as f:
    data = f.readlines()
    count = 0
    for line in data:
        (a_min, a_max, b_min, b_max) = parse_line(line)
        if fully_contains(a_min, a_max, b_min, b_max):
            count += 1
    print(count)