from typing import List

# Day X: ...

test_data = ''''''.split('\n')


def part1(data: List[str]):
    return 1


def part2(data: List[str]):
    return 1


if __name__ == '__main__':
    with open('input.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    assert part1(test_data) == 0, f'Part 1 returned {part1(test_data)}'
    print('Part 1:', part1(data))

    assert part2(test_data) == 0, f'Part 2 returned {part2(test_data)}'
    print('Part 2:', part2(data))
