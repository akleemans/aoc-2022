from typing import List

# Day 3: Rucksack Reorganization

test_data = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.split('\n')


def part1(data: List[str]):
    score = 0
    for rucksack in data:
        l = int(len(rucksack) / 2)
        comp1 = rucksack[:l]
        comp2 = rucksack[l:]
        duplicate: str = list(set(comp1).intersection(set(comp2)))[0]
        if duplicate.islower():
            score += ord(duplicate) - 96
        else:
            score += ord(duplicate) - 38
    return score


def part2(data: List[str]):
    score = 0
    for i in range(0, len(data), 3):
        duplicate: str = list(set(data[i]).intersection(set(data[i + 1])).intersection(set(data[i + 2])))[0]
        if duplicate.islower():
            score += ord(duplicate) - 96
        else:
            score += ord(duplicate) - 38
    return score


def main():
    with open('inputs/day03.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 157, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 8105, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 70, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 2363, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
