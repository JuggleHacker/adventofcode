import sys
sys.set_int_max_str_digits(100000)

class Monkey:
    def __init__(self, items, operation, divisible_by, true_monkey, false_monkey, inspections=0):
        self.inspections = inspections
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def __str__(self):
        return f"Monkey with items {self.items}, operation {self.operation}, test: {self.divisible_by}, true_monkey {self.true_monkey} and false_monkey {self.false_monkey} and inspections {self.inspections}"

def parse_monkey(list_of_attributes):
    items = list_of_attributes[0][18:]
    items = [int(x) for x in items.split(', ')]
    operation = list_of_attributes[1][19:-1]
    test = int(list_of_attributes[2][21:-1])
    true_monkey = int(list_of_attributes[3][29])
    false_monkey = int(list_of_attributes[4][30:])
    return Monkey(items, operation, test, true_monkey, false_monkey)



def next_round(list_of_monkeys, common_number):
    for monkey in list_of_monkeys:
        for worry_level in monkey.items:
            new_worry_level = eval(monkey.operation.replace('old', str(worry_level)))
            new_worry_level %= common_number
            monkey.inspections += 1
            if new_worry_level % monkey.divisible_by == 0:
                list_of_monkeys[monkey.true_monkey].items.append(new_worry_level)
            else:
                list_of_monkeys[monkey.false_monkey].items.append(new_worry_level)
        monkey.items = []

def solution(path):
    with open(path) as f:
        data = f.readlines()
        monkeys = []
        i = 1
        while i < len(data):
            monkey_to_parse = data[i:i+5]
            monkeys.append(parse_monkey(monkey_to_parse))
            i += 7
        common_number = 1
        for monkey in monkeys:
            common_number *= monkey.divisible_by
        for _ in range(10000):
            next_round(monkeys, common_number)
        inspections = sorted([monkey.inspections for monkey in monkeys])
        print(inspections)
        print(inspections[-1] * inspections[-2])



# print(solution('example_input.txt'))
print(solution('input.txt'))