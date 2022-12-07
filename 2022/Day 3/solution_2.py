alphabet = 'abcdefghijklmnopqrstuvwxyz'
priotities = alphabet + alphabet.upper()

def score(item):
    return priotities.index(item) + 1

def group_file_into(file, n):
    n_lines = [file.readline() for _ in range(n)]
    return [line[:-1] if line[-1] == '\n' else line for line in n_lines]

def first_common_character(*group_of_items):
    for char in priotities:
        if all(char in group for group in group_of_items):
            return char

# with open('example_input.txt') as f:
with open('input.txt') as f:
    total = 0
    while True:
        try:
            group = group_file_into(f, 3)
            print(group)
        except IndexError:
            break
        common_item = first_common_character(*group)
        print(common_item)
        total += score(common_item)
    print(total)