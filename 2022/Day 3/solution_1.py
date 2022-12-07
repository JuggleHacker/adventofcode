def common_item_score(backpack):
    items = len(backpack)
    pocket_1_items = backpack[:(items // 2)]
    pocket_2_items = backpack[(items // 2):]
    common_item = set(pocket_1_items).intersection(set(pocket_2_items))
    total = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    priotities = alphabet + alphabet.upper()
    for item in common_item:
        total += (priotities.index(item) + 1)
    return total

with open('input.txt') as f:
# with open('example_input.txt') as f:
    total = 0
    for backpack in f.readlines():
        backpack = backpack[:-1] if backpack[-1] == '\n' else backpack
        total += common_item_score(backpack)
    print(total)