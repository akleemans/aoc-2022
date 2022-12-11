import time
from typing import List

from monkey import Monkey

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


def create_monkeys(data: List[str], divide: bool = True) -> List[Monkey]:
    monkeys = []
    offset = 0
    while offset <= len(data):
        idx = data[offset].split(' ')[1].split(':')[0]
        start_items = [int(i) for i in data[offset + 1].split(':')[1].split(',')]
        operation = data[offset + 2].split('=')[1]
        divisible_test = int(data[offset + 3].split(' ')[-1])
        target_idx = {True: int(data[offset + 4].split(' ')[-1]), False: int(data[offset + 5].split(' ')[-1])}
        monkeys.append(Monkey(idx, start_items, operation, divisible_test, target_idx, divide, monkeys))
        offset += 7
    if not divide:
        modulo = 1
        for m in monkeys:
            modulo *= m.divisible_test
        for monkey in monkeys:
            monkey.modulo = modulo
    return monkeys


def part1(data: List[str]):
    monkeys = create_monkeys(data)

    for i in range(20):
        for monkey in monkeys:
            monkey.process_items()

    print('Monkeys:', monkeys)
    monkeys = sorted(monkeys, key=lambda m: m.items_inspected, reverse=True)
    return monkeys[0].items_inspected * monkeys[1].items_inspected


def part2(data: List[str]):
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
