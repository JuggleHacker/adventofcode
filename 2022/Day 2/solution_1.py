def score(A, B):
    # 0 for rock, 1 for paper, 2 for scissors
    choice_a = 'ABC'.index(A)
    choice_b = 'XYZ'.index(B)
    initial_score = choice_b + 1
    if choice_a == choice_b:
        return initial_score + 3
    elif (choice_a + 1) % 3 == choice_b:
        return initial_score + 6
    else:
        return initial_score

def solution(path):
    with open(path) as f:
        rounds = f.readlines()
    running_score = 0
    for round in rounds:
        player_A = round[0]
        player_B = round[2]
        running_score += score(player_A, player_B)
    return running_score

if __name__ == "__main__":
    print(solution('example_input.txt'))
    print(solution('input.txt'))
