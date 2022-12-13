from typing import List

# Day 4: Camp Cleanup

test_data = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''.split('\n')


def part1(data: List[str]):
    score = 0
    for line in data:
        a, b = line.split(',')
        a1, a2 = [int(x) for x in a.split('-')]
        b1, b2 = [int(x) for x in b.split('-')]
        if (a1 >= b1 and a2 <= b2) or (a1 <= b1 and a2 >= b2):
            score += 1
    return score


def have_overlap(a1: int, a2: int, b1: int, b2: int) -> bool:
    """Determine if two ranges a1-a2, b1-b2 have an overlap"""
    return a1 <= b1 <= a2 or b1 <= a1 <= b2


def part2(data: List[str]):
    score = 0
    for line in data:
        a, b = line.split(',')
        a1, a2 = [int(x) for x in a.split('-')]
        b1, b2 = [int(x) for x in b.split('-')]
        if have_overlap(a1, a2, b1, b2):
            score += 1
    return score


def main():
    with open('inputs/day04.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 2, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 444, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 4, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 801, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
