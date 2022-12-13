import copy
import json
from typing import List, Optional

# Day 13: Distress Signal

test_data = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''.split('\n')


def is_ordered(a, b) -> Optional[bool]:
    if isinstance(a, List) and isinstance(b, List):
        while True:
            if len(a) == 0 and len(b) == 0:
                return None
            elif len(a) == 0 and len(b) > 0:
                return True
            elif len(a) > 0 and len(b) == 0:
                return False
            else:
                a1 = a.pop(0)
                b1 = b.pop(0)
                ordered = is_ordered(a1, b1)
                if ordered is not None:
                    return ordered
    elif isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        elif a > b:
            return False
        else:
            return None
    else:
        # One int, one list
        if isinstance(a, int):
            return is_ordered([a], b)
        else:
            return is_ordered(a, [b])


def part1(data: List[str]):
    indices = []
    idx = 1
    for i in range(0, len(data), 3):
        a = json.loads(data[i])
        b = json.loads(data[i + 1])
        if is_ordered(a, b):
            indices.append(idx)
        idx += 1
    return sum(indices)


def part2_simple(data: List[str]):
    """Original version with BubbleSort"""
    entries = []
    for i in range(0, len(data), 3):
        entries.append(json.loads(data[i]))
        entries.append(json.loads(data[i + 1]))
    marker1 = [[2]]
    marker2 = [[6]]
    entries.append(marker1)
    entries.append(marker2)

    solved = False
    while not solved:
        solved = True
        for i in range(len(entries) - 1):
            if not is_ordered(copy.deepcopy(entries[i]), copy.deepcopy(entries[i + 1])):
                temp = entries[i + 1]
                entries[i + 1] = entries[i]
                entries[i] = temp
                solved = False
    return (entries.index(marker1) + 1) * (entries.index(marker2) + 1)


def part2(data: List[str]):
    """Optimized version without sorting, just counting how many elements come before the markers"""
    data = [json.loads(e) for e in data if len(e) > 1]
    marker1 = [[2]]
    idx1 = 1
    residue_list = []
    for entry in data:
        if is_ordered(copy.deepcopy(entry), copy.deepcopy(marker1)):
            idx1 += 1
        else:
            residue_list.append(entry)

    marker2 = [[6]]
    idx2 = idx1 + 1
    for entry in residue_list:
        if is_ordered(copy.deepcopy(entry), copy.deepcopy(marker2)):
            idx2 += 1

    return idx1 * idx2


def main():
    with open('inputs/day13.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 13, f'Part 1 returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 5882, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 140, f'Part 2 returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 24948, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
