from typing import List, Tuple

# Day 18: Boiling Boulders

test_data = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''.split('\n')

dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def add(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def part1(data: List[str]):
    cubes = []
    for line in data:
        a, b, c = line.split(',')
        cubes.append((int(a), int(b), int(c)))

    count = 0
    for cube in cubes:
        count += sum([1 for d in dirs if add(cube, d) not in cubes])
    return count


def part2(data: List[str]):
    cubes = []
    for line in data:
        a, b, c = line.split(',')
        cubes.append((int(a), int(b), int(c)))

    x_max = max([c[0] for c in cubes]) + 1
    y_max = max([c[1] for c in cubes]) + 1
    z_max = max([c[2] for c in cubes]) + 1
    start = (-1, -1, -1)

    score = 0
    queue = [start]
    visited_steam = []

    while len(queue) > 0:
        pos = queue.pop(0)
        if pos in visited_steam:
            continue
        else:
            visited_steam.append(pos)

        for d in dirs:
            new_pos = add(pos, d)
            if new_pos in visited_steam:
                continue
            elif new_pos[0] > x_max or new_pos[1] > y_max or new_pos[2] > z_max or \
                new_pos[0] < -1 or new_pos[1] < -1 or new_pos[2] < -1:
                continue
            elif new_pos in cubes:
                # Neighbor of lava, count surface
                score += 1
                continue
            queue.append(new_pos)
    return score


def main():
    with open('inputs/day18.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 64, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 4332, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 58, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 2524, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
