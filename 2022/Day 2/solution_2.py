def chose(A, B):
    if B == 'Y':
        return ['rock', 'paper', 'scissors']['ABC'.index(A)]
    beats = {"A" : "paper", "B": "scissors", "C": "rock"}
    if B == 'Z':
        return beats[A]
    loses = {'A': 'scissors', 'B': 'rock', 'C': 'paper'}
    if B == 'X':
        return loses[A]

def score(A, B):
    scores = {'rock': 1, 'paper': 2, 'scissors': 3}
    return [0, 3, 6]['XYZ'.index(B)] + scores[chose(A, B)]

def solution(path):
    with open(path) as f:
        rounds = f.readlines()
    running_score = 0
    for round in rounds:
        player_A = round[0]
        player_B = round[2]
        running_score += score(player_A, player_B)
    return running_score

print(solution('example_input.txt'))
print(solution('input.txt'))