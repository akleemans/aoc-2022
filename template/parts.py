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

    part1_test_result = part1(test_data)
    assert part1_test_result == 0, f'Part 1 returned {part1_test_result}'
    print('Part 1:', part1(data))

    part2_test_result = part2(test_data)
    assert part2_test_result == 0, f'Part 2 returned {part2_test_result}'
    print('Part 2:', part2(data))
