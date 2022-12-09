def visible_left_or_right(row_of_trees):
    total_visible = 2
    max_left = row_of_trees[0]
    max_right = max(row_of_trees[2:])
    for height in row_of_trees[1:-1]:
        if height > max_left or height > max_right:
            total_visible += 1
        max_left = max(max_left, height)
        max_right = max(max_right, height)

def solution(path):
    with open(path) as f:
        data = f.readlines()
        rows = len(data)
        columns = len(data[0][:-1])
        total_visible = 0
        max_above_list = [-1] * rows
        for row_number, row in enumerate(data):
            max_left = -1
            trees = row if row[-1] != "\n" else row[:-1]
            max_below_list = [-1] * rows
            for trees_to_max in data[row_number + 1:]:
                for index, height in enumerate(trees_to_max):
                    if height == '\n':
                        continue
                    max_below_list[index] = max(max_below_list[index], int(height))
            for index, height in enumerate(trees):
                max_right = -1 if index == columns - 1 else max(int(height) for height in trees[index+1:])
                if height == "\n":
                    continue
                tree_height = int(height)
                max_above = max_above_list[index]
                max_below = max_below_list[index]
                # print(f"Considering {tree_height} at ({row_number},{index})")
                if tree_height > max_left or tree_height > max_right or tree_height > max_below or tree_height > max_above:
                    # print(f"{tree_height} in column {index} is visible. Left {max_left} right {max_right} above {max_above} below {max_below}")
                    total_visible += 1
                    max_above_list[index] = max(max_above_list[index], tree_height)
                    max_left = max(max_left, tree_height)
                # else:
                #     print(f"{tree_height} in column {index} is NOT visible. Left {max_left} right {max_right} above {max_above} below {max_below}")

        print(f"Visible: {total_visible}")

solution('example_input.txt')
print(solution('input.txt'))