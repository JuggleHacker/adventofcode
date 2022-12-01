def solution(path):
    with open(path) as f:
        data = f.read().split('\n')
        elfs = []
        total = 0
        for item in data:
            if item == '':
                elfs.append(total)
                total = 0
            else:
                total += int(item)
        elfs.append(total)
        return max(elfs)

print(solution('input.txt'))