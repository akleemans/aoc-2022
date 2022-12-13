from typing import List

# Day 1: Calorie Counting

test_data = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''.split('\n')


def part1(data: List[str]):
    highest_count = 0
    count = 0
    for calories in data:
        if calories == '':
            if highest_count < count:
                highest_count = count
            count = 0
        else:
            count += int(calories)
    return highest_count


def part2(data: List[str]):
    current_count = 0
    counts = []
    for calories in data:
        if calories == '':
            counts.append(current_count)
            current_count = 0
        else:
            current_count += int(calories)
    counts.append(current_count)

    counts.sort(reverse=True)
    return sum(counts[:3])


def main():
    with open('inputs/day01.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 24000, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 69795, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 45000, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 208437, f'Part 2 returned {part1_result}'


if __name__ == '__main__':
    main()
