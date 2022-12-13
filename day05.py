from typing import List

# Day 5: Supply Stacks

test_data = '''    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''.split('\n')


def index_of_first(l: List[str], predicate):
    for i, v in enumerate(l):
        if predicate(v):
            return i


def prepare_stack(data: List[str]) -> List[List[str]]:
    # First, find index
    bottom_line = index_of_first(data, lambda x: x.startswith(' 1'))

    # Initialize stacks
    amount_of_stacks = int(data[bottom_line].split(' ')[-1])
    stacks = [[] for _ in range(amount_of_stacks)]
    positions = []

    # Collect positions
    for i in range(len(data[bottom_line])):
        if data[bottom_line][i] != ' ':
            positions.append(i)

    for line_nr in range(bottom_line - 1, -1, -1):
        for x in range(len(positions)):
            if len(data[line_nr]) < positions[x]:
                continue
            n = data[line_nr][positions[x]]
            if n != ' ':
                stacks[x].append(n)
    return stacks


def part1(data: List[str]):
    stacks = prepare_stack(data)

    # Prepare instruction
    instructions = []
    flag = False
    for line in data:
        if line.startswith('move'):
            flag = True
        if flag:
            instructions.append(line)

    # Execute instructions
    for instruction in instructions:
        parts = instruction.split(' ')
        amount, source, target = int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1

        for i in range(amount):
            crate = stacks[source].pop()
            stacks[target].append(crate)

    return ''.join([x[-1] for x in stacks])


def part2(data: List[str]):
    stacks = prepare_stack(data)

    # Prepare instruction
    instructions = []
    flag = False
    for line in data:
        if line.startswith('move'):
            flag = True
        if flag:
            instructions.append(line)

    # Execute instructions
    for instruction in instructions:
        parts = instruction.split(' ')
        amount, source, target = int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1

        # print('starting with:', stacks[source])
        crates = stacks[source][-amount:]
        # print('  taking crates =', crates)
        stacks[source] = stacks[source][:-amount]
        # print('  leaving =', stacks[source])
        stacks[target].extend(crates)

    return ''.join([x[-1] for x in stacks])


def main():
    with open('inputs/day05.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 'CMZ', f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 'BSDMQFLSP', f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 'MCD', f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 'PGSQBFLDP', f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
