from typing import List, Tuple

# Day 14: Regolith Reservoir

test_data = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''.split('\n')


def get_coords(data):
    coords: List = []
    for line in data:
        last = None
        for pair in line.split(' -> '):
            a, b = pair.split(',')
            current = (int(a), int(b))
            if last is not None:
                coords.append((last, current))
            last = current

    # Normalize, so part 1 shows up on resized grid
    #x_min = 10000
    #for (start, end) in coords:
    #    x_min = min(start[0], x_min)
    #    x_min = min(end[0], x_min)
    # print('x_min:', x_min)
    # for i in range(len(coords)):
    #    coords[i] = (coords[i][0][0] - x_min, coords[i][0][1]), (coords[i][1][0] - x_min, coords[i][1][1])
    return coords, 0  # x_min


def draw_map(m):
    for line in m:
        print(''.join(line))
    input()


def build_map(coords: List[List[Tuple[int, int]]]) -> List[List[str]]:
    x_max, y_max = 0, 0
    for (start, end) in coords:
        x_max = max(start[0], x_max)
        x_max = max(end[0], x_max)
        y_max = max(start[1], y_max)
        y_max = max(end[1], y_max)

    m = [['.' for _ in range(x_max + 1)] for _ in range(y_max + 1)]
    # draw_map(m)

    for (start, end) in coords:
        if start[0] == end[0]:
            a = min(start[1], end[1])
            b = max(start[1], end[1])
            for i in range(a, b + 1):
                m[i][start[0]] = '#'
        else:
            a = min(start[0], end[0])
            b = max(start[0], end[0])
            for i in range(a, b + 1):
                m[start[1]][i] = '#'

    return m


def move(m, pos) -> Tuple[int, int]:
    x, y = pos
    if m[y + 1][x] == '.':
        return x, y + 1
    elif m[y + 1][x - 1] == '.':
        return x - 1, y + 1
    elif m[y + 1][x + 1] == '.':
        return x + 1, y + 1
    else:
        return pos


def pour_sand(m, s):
    finished = False
    while True:
        # If source blocked, stop
        if m[s[1]][s[0]] == 'o':
            break

        pos = (s[0], s[1])
        while True:
            try:
                pos_next = move(m, pos)
            except IndexError:
                finished = True
                break
            if pos_next == pos:
                m[pos[1]][pos[0]] = 'o'
                break
            pos = pos_next
        if finished:
            break

    return m


def part1(data: List[str]):
    coords, x_min = get_coords(data)
    # print('coords:', coords)
    sand_source = (500 - x_min, 0)
    # print('Sand source:', sand_source)
    m = build_map(coords)
    m[sand_source[1]][sand_source[0]] = '+'
    # print('Map:')
    # draw_map(m)
    m = pour_sand(m, sand_source)

    return sum(line.count('o') for line in m)


def part2(data: List[str]):
    coords, x_min = get_coords(data)
    sand_source = (500 - x_min, 0)

    y_max = 0
    for (start, end) in coords:
        y_max = max(start[1], y_max)
        y_max = max(end[1], y_max)
    coords.append(((0, y_max + 2), (1000, y_max + 2)))
    m = build_map(coords)

    m[sand_source[1]][sand_source[0]] = '+'
    m = pour_sand(m, sand_source)

    return sum(line.count('o') for line in m)


def main():
    with open('inputs/day14.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 24, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 755, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 93, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 29805, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
