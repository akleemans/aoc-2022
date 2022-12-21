import operator
from typing import List, Dict

# Day 21: Monkey Math

test_data = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''.split('\n')


class Monkey:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.operator = None

    def get_value(self) -> int:
        if self.value is not None:
            return self.value
        return self.operator(self.left.get_value(), self.right.get_value())

    def set(self, left, op, right):
        self.left = left
        self.right = right
        self.operator = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}[op]


def initialize_monkeys(data) -> Dict[str, Monkey]:
    # Round 1: init
    monkey_dict = {}
    for line in data:
        key = line.split(':')[0]
        monkey_dict[key] = Monkey()

    # Round 2:
    for line in data:
        key, value = line.split(': ')
        if ' ' not in value:
            monkey_dict[key].value = int(value)
        else:
            a, op, b = value.split(' ')
            monkey_dict[key].set(monkey_dict[a], op, monkey_dict[b])

    return monkey_dict


def part1(data: List[str]):
    root_monkey = initialize_monkeys(data)['root']
    return root_monkey.get_value()


def part2(data: List[str]):
    monkey_dict = initialize_monkeys(data)

    for line in data:
        if line.startswith('root'):
            a, b = line.split(': ')[1].split(' + ')
            monkey_a, monkey_b = monkey_dict[a], monkey_dict[b]
            break


    value1 = 1
    value2 = 2
    count = 0
    i = 0
    while value1 != value2:
        i -= 1
        count += 1
        monkey_dict['humn'].value = i
        value1 = monkey_a.get_value()
        value2 = monkey_b.get_value()
        if count % 1000 == 0:
            print(f'i = {i}, {value1} {value2}')

    return i


def main():
    with open('inputs/day21.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 152, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 170237589447588, f'Part 1 returned {part1_result}'

    #part2_test_result = part2(test_data)
    #assert part2_test_result == 301, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 3712643961892, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
