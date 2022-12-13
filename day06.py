from typing import List

# Day 6: Tuning Trouble

test_data = '''zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'''.split('\n')


def part1(data: List[str]):
    line = data[0]
    for i in range(4, len(line), 1):
        last_four = line[i - 4:i]
        if len(last_four) == len(set(last_four)):
            return i


def part2(data: List[str]):
    line = data[0]
    for i in range(14, len(line), 1):
        last_range = line[i - 14:i]
        if len(last_range) == len(set(last_range)):
            return i


def main():
    with open('inputs/day06.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 11, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 1896, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 26, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 3452, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
