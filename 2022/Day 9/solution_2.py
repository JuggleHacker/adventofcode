from solution_1 import *

def solution(path):
    with open(path) as f:
        data = f.readlines()
    initial_positions = [(0,0) for _ in range(10)]
    tail_positions = {initial_positions[-1]}
    for instruction in data:
        (direction, times) = instruction.split(' ')
        for _ in range(int(times)):
            initial_positions[0] = move_in_direction(initial_positions[0], direction)
            for i in range(1, len(initial_positions)):
                initial_positions[i] = move_after_head(initial_positions[i-1], initial_positions[i])
            tail_positions.add(initial_positions[-1])
    return len(tail_positions)

if __name__ == "__main__":
    print(solution('example_input.txt'))
    print(solution('input.txt'))