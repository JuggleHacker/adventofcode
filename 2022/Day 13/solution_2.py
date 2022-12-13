import json
from solution_1 import in_order

def bubble_sort(input_list, in_order):
    for j in range(len(input_list)):
        for i in range(len(input_list)-1-j):
            if not in_order(input_list[i], input_list[i+1]):
                input_list[i+1], input_list[i] = input_list[i], input_list[i+1]
    return input_list

def solution(path):
    with open(path) as f:
        data = f.readlines()
        all_lines = [json.loads(line) for line in data[0::3] + data[1::3]] + [[[2]]] + [[[6]]]
        sorted_lines = bubble_sort(all_lines, in_order)
        x = sorted_lines.index([[2]]) + 1
        y = sorted_lines.index([[6]]) + 1
        return x * y


print(solution('example_input.txt'))
print(solution('input.txt'))