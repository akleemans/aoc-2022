from typing import List, Dict, Optional

# Day 23: Unstable Diffusion

test_data = '''....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..'''.split('\n')


class Coord:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def add(self, other: 'Coord'):
        return Coord(self.x + other.x, self.y + other.y)

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        # return (self.x, self.y).__eq__((other.x, other.y))
        if other is None:
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (self.x, self.y).__hash__()
        # return self.x * 10**4 + self.y


def get_elves(data) -> List[Coord]:
    elves = []
    for y in range(len(data)):
        line = data[y]
        for x in range(len(line)):
            if line[x] == '#':
                elves.append(Coord(x, y))
    return elves


def get_possible_move(elf, elves, directions) -> Optional[Coord]:
    # Check if elf has neighbors, if not,
    neighbors = 0
    for d in [Coord(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x, y) != (0, 0)]:
        target = elf.add(d)
        if target in elves:
            neighbors += 1
            break
    if neighbors == 0:
        return None

    for d in directions:
        target = elf.add(d)
        mod_x = 1 if d.x == 0 else 0
        mod_y = 1 if d.y == 0 else 0
        a = Coord(target.x + mod_x, target.y + mod_y)
        b = Coord(target.x - mod_x, target.y - mod_y)
        if target not in elves and a not in elves and b not in elves:
            # print('Elf', elf, 'will try to move to', target)
            # print(f'{target} not in {elves}', target not in elves)
            # input()
            return target
    return None


def get_propositions(elves, directions) -> Dict[Coord, Coord]:
    propositions = {}
    for elf in elves:
        propositions[elf] = get_possible_move(elf, elves, directions)
    return propositions


def execute_moves(elves: List[Coord], propositions: Dict[Coord, Coord]) -> bool:
    moved = False
    targets = list(propositions.values())

    for elf, target in propositions.items():
        if target is None:
            continue
        # If single candidate for target, do the move
        if targets.count(target) == 1:
            moved = True
            elves.remove(elf)
            elves.append(target)
        # else:
        #    print(f'Elf {elf} doesnt move')
    return moved


def draw_map(elves):
    min_x = min(elf.x for elf in elves)
    max_x = max(elf.x for elf in elves)
    min_y = min(elf.y for elf in elves)
    max_y = max(elf.y for elf in elves)

    m = []
    for y in range(min_y, max_y + 1):
        line = []
        for x in range(min_x, max_x + 1):
            s = '.'
            if Coord(x, y) in elves:
                s = '#'
            line.append(s)
        m.append(line)

    print('Map:')
    for line in m:
        print(''.join(line))
    input()


def part1(data: List[str]):
    elves = get_elves(data)
    # print('Initial elves:', elves)
    # N, S, W, E
    directions = [Coord(0, -1), Coord(0, 1), Coord(-1, 0), Coord(1, 0)]

    for round in range(10):
        print(f'Round {round}, dirs={directions}')
        propositions = get_propositions(elves, directions)
        elves = execute_moves(elves, propositions)

        d = directions.pop(0)
        directions.append(d)
        # draw_map(elves)
        # break

    min_x = min(elf.x for elf in elves)
    max_x = max(elf.x for elf in elves)
    min_y = min(elf.y for elf in elves)
    max_y = max(elf.y for elf in elves)

    total = (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)
    # print('Elves:', elves, 'total:', total)
    return total


def part2(data: List[str]):
    elves = get_elves(data)
    # N, S, W, E
    directions = [Coord(0, -1), Coord(0, 1), Coord(-1, 0), Coord(1, 0)]

    round = 1
    while True:
        # if round % 100 == 0:
        # print('Round:', round)
        propositions = get_propositions(elves, directions)
        if not execute_moves(elves, propositions):
            break
        d = directions.pop(0)
        directions.append(d)
        round += 1

    return round


def main():
    with open('inputs/day23.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 110, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 4158, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 20, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 1014, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
