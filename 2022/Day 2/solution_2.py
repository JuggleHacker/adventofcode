from solution_1 import score

def score_from_outcome(A, outcome):
    # 0 for rock, 1 for paper, 2 for scissors
    choice_a = 'ABC'.index(A)
    # 0 for draw, 1 for win, 2 for lose
    result = 'YZX'.index(outcome)
    b_choice = (choice_a + result) % 3
    return score(A, 'XYZ'[b_choice])

def solution(path):
    with open(path) as f:
        rounds = f.readlines()
    running_score = 0
    for round in rounds:
        player_A = round[0]
        player_B = round[2]
        running_score += score_from_outcome(player_A, player_B)
    return running_score

if __name__ == "__main__":
    print(solution('example_input.txt'))
    print(solution('input.txt'))
