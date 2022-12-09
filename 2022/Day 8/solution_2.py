def scenic_score(height, row, col, grid):
    # print(f"At {row}, {col} height {height}")
    left = 0
    right = 0
    up = 0
    down = 0
    left_index = col - 1
    while left_index >= 0 and grid[row][left_index] < height:
        left += 1
        left_index -= 1
    if left_index != -1:
        left += 1
    # print(f"Left: {left}")
    if left == 0:
        return 0
    right_index = col + 1
    while right_index < len(grid[0]) and grid[row][right_index] < height:
        right += 1
        right_index += 1
    if right_index != len(grid[0]):
        right += 1
    # print(f"Right: {right}")
    if right == 0:
        return 0
    up_index = row - 1
    while up_index >= 0 and grid[up_index][col] < height:
        up += 1
        up_index -= 1
    if up_index != -1:
        up += 1
    # print(f"Up: {up}")
    if up == 0:
        return 0
    down_index = row + 1
    while down_index < len(grid) and grid[down_index][col] < height:
        down += 1
        down_index += 1
    if down_index != len(grid):
        down += 1
    # print(f"Down: {down}")
    return left * right * up * down

def solution(path):
    with open(path) as f:
        data = f.readlines()
        grid = []
        for row in data:
            tree_heights = row[:-1] if row[-1] == "\n" else row
            grid.append([int(height) for height in tree_heights])
        max_scenic_score = 0
        for row_number, row in enumerate(grid):
            for col_number, tree_height in enumerate(row):
                this_scenic_score = scenic_score(tree_height, row_number, col_number, grid)
                max_scenic_score = max(max_scenic_score, this_scenic_score)
        print(max_scenic_score)

# print(solution('example_input.txt'))
print(solution('input.txt'))