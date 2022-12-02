def score(A, B):
    beats = {"A" : "Y", "B": "Z", "C": "X"}
    scores = {"X": 1, "Y": 2, "Z": 3}
    if B == beats[A]:
        return 6 + scores[B]
    elif "ABC".index(A) == "XYZ".index(B):
        return 3 + scores[B]
    else:
        return scores[B]

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