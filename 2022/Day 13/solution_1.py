import json

def are_equal(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            return left == right
        else:
            return are_equal([left], right)
    if isinstance(right, int):
        return are_equal(left, [right])
    if len(left) != len(right):
        return False
    for item_number, left_item in enumerate(left):
        right_item = right[item_number]
        if isinstance(left_item, int):
            if isinstance(right_item, int):
                if left_item != right_item:
                    return False
            else:
                if not are_equal(left[:item_number] + [[left[item_number]]] + left[item_number+1:], right):
                    return False
        else:
            if isinstance(right_item, int):
                if not are_equal(left, right[:item_number] + [[right[item_number]]] + right[item_number+1:]):
                    return False
            else:
                if not are_equal(left_item, right_item):
                    return False
    return True


def in_order(left, right):
    i = 0
    while True:
        try:
            left_item = left[i]
        except:
            return True
        try:
            right_item = right[i]
        except:
            return False
        if are_equal(left_item, right_item):
            i += 1
            continue
        if isinstance(left_item, int):
            if isinstance(right_item, int):
                return left_item < right_item
            else:
                return in_order([[left_item]], right_item)
        else:
            if isinstance(right_item, list):
                return in_order(left_item, right_item)
            else:
                return in_order(left_item, [right_item])

def solution(path):
    with open(path) as f:
        data = f.readlines()
        i = 0
        count = 0
        while i < len(data):
            first = data[i]
            second = data[i+1]
            if in_order(json.loads(first), json.loads(second)):
                to_add = (1 + i // 3)
                count += to_add
            i += 3
        return count


if __name__ == "__main__":
    print(solution('example_input.txt'))
    print(solution('input.txt'))