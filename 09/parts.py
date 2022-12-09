from typing import List, Tuple

# Day 9: Rope Bridge

test_data = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.split('\n')

test_data2 = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''.split('\n')

dir_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def walk(pos, direction: str) -> Tuple[int, int]:
    return add(pos, dir_map[direction])


def add(a, b):
    return tuple(map(lambda i, j: i + j, a, b))


def subtract(a, b):
    return tuple(map(lambda i, j: i - j, a, b))


def normalize(t: Tuple[int, int]) -> Tuple[int, int]:
    a = t[0] // abs(t[0]) if t[0] != 0 else 0
    b = t[1] // abs(t[1]) if t[1] != 0 else 0
    return (a, b)


def follow(pos, follower) -> Tuple[int, int]:
    diff = subtract(pos, follower)
    # no change needed
    if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
        return follower
    else:
        return add(follower, normalize(diff))


def part1(data: List[str]):
    follower_path = []
    pos = (0, 0)
    follower = (0, 0)

    for line in data:
        direction, amount = line.split(' ')
        amount = int(amount)
        for i in range(amount):
            # print('Walking', direction, 'pos:', pos)
            pos = walk(pos, direction)
            # print('...pos:', pos)

            follower = follow(pos, follower)
            # print('...follower:', follower)
            follower_path.append(follower)

    return len(set(follower_path))


def part2(data: List[str]):
    follower_path = []
    nodes = [(0, 0) for _ in range(10)]

    for line in data:
        direction, amount = line.split(' ')
        amount = int(amount)
        for i in range(amount):
            nodes[0] = walk(nodes[0], direction)
            for i in range(1, 10):
                nodes[i] = follow(nodes[i - 1], nodes[i])
            follower_path.append(nodes[-1])
    return len(set(follower_path))


if __name__ == '__main__':
    with open('input.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    assert part1(test_data) == 13, f'Part 1 returned {part1(test_data)}'
    print('Part 1:', part1(data))

    assert part2(test_data2) == 36, f'Part 2 returned {part2(test_data)}'
    print('Part 2:', part2(data))
