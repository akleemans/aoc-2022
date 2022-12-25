from typing import List, Tuple, Set

# Day 24: Blizzard Basin

test_data = '''#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#'''.split('\n')


class Coord:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.pair = (x, y)

    def add(self, other: 'Coord'):
        return Coord(self.x + other.x, self.y + other.y)

    def __str__(self):
        return str(self.pair)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.pair == other.pair

    def __hash__(self):
        return (self.x, self.y).__hash__()


directions = {'v': Coord(0, 1), '^': Coord(0, -1), '<': Coord(-1, 0), '>': Coord(1, 0), 'x': Coord(0, 0)}
width = 0
height = 0


def get_blizzards(data):
    blizzards: List[Tuple[Coord, str]] = []
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            c = data[y][x]
            if c != '.':
                blizzards.append((Coord(x, y), c))
    return blizzards


def move_blizzards(old_blizzards: List[Tuple[Coord, str]]) -> List[Tuple[Coord, str]]:
    new_blizzards = []
    for blizzard in old_blizzards:
        # print('Moving blizzard', blizzard, '...')
        direction = directions[blizzard[1]]
        new_pos = blizzard[0].add(direction)
        # print('...with new pos', new_pos)
        # print('new_pos.x:', new_pos.x, ' == 0:', new_pos.x == 0)
        # print('new_pos.y:', new_pos.y, ' == 0:', new_pos.y == 0)

        # If blizzard reaches wall, wrap around
        if new_pos.x == 0:
            # new_pos.x = width - 2
            new_pos = Coord(width - 2, new_pos.y)
        elif new_pos.x == width - 1:
            new_pos = Coord(1, new_pos.y)
            # new_pos.x = 1
        elif new_pos.y == 0:
            new_pos = Coord(new_pos.x, height - 2)
            # print('....new_pos:', new_pos)
        elif new_pos.y == height - 1:
            new_pos = Coord(new_pos.x, 1)
            # new_pos.y = 1

        # print('...to new pos', new_pos)
        new_blizzards.append((new_pos, blizzard[1]))
    # input()

    return new_blizzards


def get_possible_positions(old_positions: Set[Coord], blizzards: List[Tuple[Coord, str]], start, target):
    new_positions = set()
    blizzard_positions = set(map(lambda b: b[0], blizzards))

    for old_pos in old_positions:
        for d in 'xv^<>':
            direction = directions[d]
            new_pos = old_pos.add(direction)
            if new_pos == start or new_pos == target:
                new_positions.add(new_pos)
            elif 1 <= new_pos.x <= width - 2 and 1 <= new_pos.y <= height - 2 and new_pos not in blizzard_positions:
                new_positions.add(new_pos)

    return new_positions


def draw_map(my_positions, blizzards):
    blizzard_positions = set(map(lambda b: b[0], blizzards))

    for y in range(height):
        row = ''
        for x in range(width):
            pos = Coord(x, y)
            if pos in my_positions:
                row += 'E'
            elif pos in blizzard_positions:
                row += '*'
            elif x == 0 or y == 0 or x == width - 1 or y == height - 1:
                row += '#'
            else:
                row += '.'
        print(row)

    input('(map drawn)')


def part1(data: List[str]):
    global width
    global height
    width = len(data[0])
    height = len(data)

    start = Coord(1, 0)
    target = Coord(data[-1].find('.'), len(data) - 1)
    blizzards = get_blizzards(data)

    my_positions = set()
    my_positions.add(start)
    t = 0
    while target not in my_positions:
        # if t % 100 == 0:
        #    print(f't={t}')
        # draw_map(my_positions, blizzards)
        blizzards = move_blizzards(blizzards)
        my_positions = get_possible_positions(my_positions, blizzards, start, target)
        t += 1

    return t


def part2(data: List[str]):
    global width
    global height
    width = len(data[0])
    height = len(data)

    start = Coord(1, 0)
    target = Coord(data[-1].find('.'), len(data) - 1)
    blizzards = get_blizzards(data)

    my_positions = {start}
    t = 0
    count = 0
    next_goal = target
    while count < 3:
        # if t % 100 == 0:
        #    print(f't={t}')
        blizzards = move_blizzards(blizzards)
        my_positions = get_possible_positions(my_positions, blizzards, start, target)

        if next_goal in my_positions:
            count += 1
            if count == 1:
                next_goal = start
                my_positions = {target}
            elif count == 2:
                next_goal = target
                my_positions = {start}
        t += 1

    return t


def main():
    with open('inputs/day24.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 18, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 262, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 54, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 785, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
