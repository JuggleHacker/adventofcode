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
        elfs.sort()
        return sum(elfs[-3:])

print(solution('input.txt'))