def first_index_of_marker(string):
    for index, character in enumerate(data):
        possible_marker = data[index: index + 4]
        if len(set(possible_marker)) == 4:
            print(possible_marker)
            return index + 4

# with open('example_input.txt') as f:
with open('input.txt') as f:
    data = f.read()
    print(data)
    print(first_index_of_marker(data))