import time
from typing import List, Dict, Optional


class Monkey:
    items_inspected: int
    idx: str
    items: List[int]
    operation: str
    divide: bool
    divisible_test: int
    target_idx: Dict[bool, int]
    monkey_list: List['Monkey']
    modulo: Optional[int]

    def __init__(self, idx: str, start_items, operation: str, divisible_test: int,
        target_idx, divide: bool):
        self.items_inspected = 0
        self.idx = idx
        self.items = start_items
        self.operation = operation
        self.divide = divide
        self.divisible_test = divisible_test
        self.target_idx = target_idx
        self.modulo = None

    def process_items(self):
        while len(self.items) > 0:
            item = self.items.pop(0)
            target, updated_item = self.process_item(item)
            target_monkey: Monkey = self.monkey_list[target]
            if not self.divide:
                updated_item %= self.modulo
            target_monkey.add_item(updated_item)

    def process_item(self, item: int):
        self.items_inspected += 1
        query = self.operation.replace('old', str(item))
        result = self.custom_eval(query)
        if self.divide:
            result = result // 3
        # print(self, 'is doing', self.operation, ':', query, '=', result)
        return self.target_idx[result % self.divisible_test == 0], result

    def custom_eval(self, s: str) -> int:
        parts = s.split(' ')
        if parts[1] == '*':
            return int(parts[0]) * int(parts[2])
        else:  # must be +
            return int(parts[0]) + int(parts[2])

    def add_item(self, item: int):
        self.items.append(item)

    def __str__(self):
        # return 'Monkey ' + self.idx + ' [' + str(self.items_inspected) + ']'
        return 'Monkey ' + self.idx + ' (' + str(self.items_inspected) + ') ' + str(self.items)

    def __repr__(self):
        return self.__str__()


# Day 11: Monkey in the Middle

test_data = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''.split('\n')


def create_monkeys(data, divide: bool = True):
    monkeys: List[Monkey] = []
    offset = 0
    while offset <= len(data):
        idx = data[offset].split(' ')[1].split(':')[0]
        start_items = [int(i) for i in data[offset + 1].split(':')[1].split(',')]
        operation = data[offset + 2].split('=')[1].strip()
        divisible_test = int(data[offset + 3].split(' ')[-1])
        target_idx = {True: int(data[offset + 4].split(' ')[-1]), False: int(data[offset + 5].split(' ')[-1])}
        monkeys.append(Monkey(idx, start_items, operation, divisible_test, target_idx, divide))
        offset += 7
    for m in monkeys:
        m.monkey_list = monkeys
    if not divide:
        modulo = 1
        for m in monkeys:
            modulo *= m.divisible_test
        for monkey in monkeys:
            monkey.modulo = modulo
    return monkeys


def part1(data):
    monkeys = create_monkeys(data)

    for i in range(20):
        for monkey in monkeys:
            monkey.process_items()

    print('Monkeys:', monkeys)
    monkeys = sorted(monkeys, key=lambda m: m.items_inspected, reverse=True)
    return monkeys[0].items_inspected * monkeys[1].items_inspected


def part2(data):
    monkeys = create_monkeys(data, False)

    for i in range(10_000):
        if i % 1000 == 0:
            print('Round:', i)
        for monkey in monkeys:
            monkey.process_items()

    print('Monkeys:', monkeys)
    monkeys = sorted(monkeys, key=lambda m: m.items_inspected, reverse=True)
    return monkeys[0].items_inspected * monkeys[1].items_inspected


if __name__ == '__main__':
    t = time.time()
    with open('input.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 10605, f'Part 1 returned {part1_test_result}'
    print('Part 1:', part1(data))

    part2_test_result = part2(test_data)
    assert part2_test_result == 2713310158, f'Part 2 returned {part2_test_result}'
    print('Part 2:', part2(data))
    print('Finished in', time.time() - t, 's')
