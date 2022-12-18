from typing import List

# Day 17: Pyroclastic Flow

test_data = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''.split('\n')


def get_height(chamber, height_baseline):
    while '#' in chamber[height_baseline]:
        height_baseline += 1
    return height_baseline


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


def get_rock(shape: str, height: int) -> List[Coord]:
    if shape == '-':
        return [Coord(x, height) for x in range(2, 6)]
    elif shape == '+':
        return [Coord(3, height), Coord(2, height + 1), Coord(3, height + 1), Coord(4, height + 1),
                Coord(3, height + 2)]
    elif shape == 'L':
        return [Coord(2, height), Coord(3, height), Coord(4, height), Coord(4, height + 1), Coord(4, height + 2)]
    elif shape == 'I':
        return [Coord(2, height), Coord(2, height + 1), Coord(2, height + 2), Coord(2, height + 3)]
    elif shape == 'O':
        return [Coord(2, height), Coord(3, height), Coord(2, height + 1), Coord(3, height + 1)]
    else:
        raise Exception(f'Shape "{shape}" unknown!')


def remove_rock(chamber, rock: List[Coord]):
    for pos in rock:
        chamber[pos.y][pos.x] = '.'


def insert_rock(chamber, rock: List[Coord]):
    for pos in rock:
        chamber[pos.y][pos.x] = '#'


def move_wind(chamber, rock: List[Coord], dir: str) -> List[Coord]:
    d = -1 if dir == '<' else 1
    updated_rock = [Coord(p.x + d, p.y) for p in rock]
    for pos in updated_rock:
        if pos.x < 0 or pos.x > 6 or chamber[pos.y][pos.x] == '#':
            return rock
    return updated_rock


def move_down(chamber, rock: List[Coord]) -> List[Coord]:
    # Update and then see if positions are possible
    updated_rock = [Coord(p.x, p.y - 1) for p in rock]
    for pos in updated_rock:
        if pos.y < 0 or chamber[pos.y][pos.x] == '#':
            return rock
    return updated_rock


def print_chamber(chamber, y):
    for line in chamber[max(0, y - 5): y + 5][::-1]:
        print(''.join(line))
    input()


def get_cycle_hash(chamber, y):
    h = ''
    for line in chamber[y - 10:y + 1][::-1]:
        h += ''.join(line)
    return h


def part1(data: List[str]):
    return build_tower(data, 2022)


def part1_old(data: List):
    rocks_stopped = 0
    wind = data[0]
    wind_idx = -1
    rocks = ['-', '+', 'L', 'I', 'O']
    rock_idx = 0
    height_baseline = 0
    insert_space = 3
    max_height = 4 * 10 ** 3
    chamber = [['.' for _ in range(7)] for _ in range(max_height)]

    # Add first block
    rock = rocks[rock_idx]
    current_rock_pos = get_rock(rock, height_baseline + insert_space)
    rock_idx += 1

    while rocks_stopped < 2022:
        # First, wind
        wind_idx = (wind_idx + 1) % len(wind)
        current_wind = wind[wind_idx]
        # Remove, then check if can be moved
        remove_rock(chamber, current_rock_pos)
        next_rock_pos = move_wind(chamber, current_rock_pos, current_wind)
        insert_rock(chamber, next_rock_pos)
        current_rock_pos = next_rock_pos

        # Move down one unit
        remove_rock(chamber, current_rock_pos)
        next_rock_pos = move_down(chamber, current_rock_pos)
        insert_rock(chamber, next_rock_pos)

        if current_rock_pos == next_rock_pos:
            # Place new block
            next_rock = rocks[rock_idx]
            rock_idx = (rock_idx + 1) % len(rocks)
            height_baseline = get_height(chamber, height_baseline)
            current_rock_pos = get_rock(next_rock, height_baseline + insert_space)
            rocks_stopped += 1
            # print_chamber(chamber, height_baseline)
        else:
            current_rock_pos = next_rock_pos
    total_height = get_height(chamber, height_baseline)
    # print('Total height:', total_height)
    return total_height


def part2(data: List[str]):
    return build_tower(data, 1_000_000_000_000)


def build_tower(data: List[str], amount_of_rocks: int):
    rocks_stopped = 0
    wind = data[0]
    wind_idx = -1
    rocks = ['-', '+', 'L', 'I', 'O']
    rock_idx = 0
    height_baseline = 0
    insert_space = 3
    max_height = 2 * 10 ** 3
    chamber = [['.' for _ in range(7)] for _ in range(max_height)]

    # Add first block
    rock = rocks[rock_idx]
    current_rock_pos = get_rock(rock, height_baseline + insert_space)
    rock_idx += 1
    cut_height = 0

    # Cycle stuff
    cycle_detection = amount_of_rocks > 10 ** 4
    cycle_rocks_stopped = 0
    cycle_hash = None
    cycle_height_base = 0

    while rocks_stopped < amount_of_rocks:
        # Cut chamber if coordinates go to high
        if height_baseline > max_height - 100:
            cut_amount = max_height // 2
            height_baseline -= cut_amount
            new_chamber = [chamber[cut_amount + i] for i in range(cut_amount)]
            new_chamber.extend([['.' for _ in range(7)] for _ in range(cut_amount)])
            chamber = new_chamber
            current_rock_pos = [Coord(pos.x, pos.y - cut_amount) for pos in current_rock_pos]
            cut_height += cut_amount
            # print('current_rock_pos after cutting:', current_rock_pos)
            # input()

        # if rocks_stopped % 100_000 == 0:
        #    print('rocks_stopped:', rocks_stopped)

        # First, wind
        wind_idx = (wind_idx + 1) % len(wind)
        current_wind = wind[wind_idx]
        # Remove, then check if can be moved
        remove_rock(chamber, current_rock_pos)
        next_rock_pos = move_wind(chamber, current_rock_pos, current_wind)
        insert_rock(chamber, next_rock_pos)
        current_rock_pos = next_rock_pos

        # Move down one unit
        remove_rock(chamber, current_rock_pos)
        next_rock_pos = move_down(chamber, current_rock_pos)
        insert_rock(chamber, next_rock_pos)

        if current_rock_pos == next_rock_pos:
            # Place new block
            next_rock = rocks[rock_idx]
            rock_idx = (rock_idx + 1) % len(rocks)
            height_baseline = get_height(chamber, height_baseline)
            current_rock_pos = get_rock(next_rock, height_baseline + insert_space)
            rocks_stopped += 1
            # print_chamber(chamber, height_baseline)

            if rocks_stopped > 1000 and rock_idx == 1 and cycle_detection:
                if cycle_hash is None:
                    cycle_hash = get_cycle_hash(chamber, height_baseline)
                    cycle_rocks_stopped = rocks_stopped
                    cycle_height_base = get_height(chamber, height_baseline) + cut_height
                else:
                    current_cycle_hash = get_cycle_hash(chamber, height_baseline)
                    if current_cycle_hash == cycle_hash:
                        current_height = get_height(chamber, height_baseline) + cut_height
                        rocks_diff = rocks_stopped - cycle_rocks_stopped
                        height_diff = current_height - cycle_height_base
                        remaining_cycles = amount_of_rocks // rocks_diff - (1000 // rocks_diff) - 2
                        # print('Cycle detected, rocks_diff:', rocks_diff, 'height_diff:', height_diff,
                        #       'remaining_cycles', remaining_cycles)
                        rocks_stopped += rocks_diff * remaining_cycles
                        cut_height += height_diff * remaining_cycles
                        cycle_detection = False
        else:
            current_rock_pos = next_rock_pos
    total_height = get_height(chamber, height_baseline) + cut_height
    # print('Total height:', total_height)
    return total_height


def main():
    with open('inputs/day17.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 3068, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 3193, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 1514285714288, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 1577650429835, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
