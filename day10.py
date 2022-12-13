from typing import List

# Day 10: Cathode-Ray Tube

test_data = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''.split('\n')

command_duration = {'addx': 2, 'noop': 1}


def part1(data: List[str]):
    signal_strengths = 0
    cycle = 1
    instruction_idx = 0
    current_command = ''
    current_duration = 0
    X = 1

    while True:
        # Fetch new command
        if current_command == '':
            current_command = data[instruction_idx]
            current_duration = 1
            instruction_idx += 1
            if instruction_idx == len(data):
                break
        elif current_command.startswith('addx'):
            current_duration += 1

        # Catch
        if (cycle - 20) % 40 == 0:
            # print('cycle:', cycle, 'X:', X)
            signal_strengths += X * cycle

        # Process command

        if command_duration[current_command.split(' ')[0]] == current_duration:
            if current_command.startswith('addx'):
                value = int(current_command.split(' ')[1])
                X += value
                current_command = ''
            elif current_command.startswith('noop'):
                current_command = ''
        cycle += 1

    return signal_strengths


def part2(data: List[str]) -> str:
    display = ''
    cycle = 0
    instruction_idx = 0
    current_command = ''
    current_duration = 0
    X = 1

    while True:
        # Fetch new command
        if current_command == '':
            if instruction_idx == len(data):
                break
            current_command = data[instruction_idx]
            current_duration = 1
            instruction_idx += 1
        elif current_command.startswith('addx'):
            current_duration += 1

        # Draw
        if cycle % 40 in [X - 1, X, X + 1]:
            display += '#'
        else:
            display += '.'

        # Process command
        if command_duration[current_command.split(' ')[0]] == current_duration:
            if current_command.startswith('addx'):
                value = int(current_command.split(' ')[1])
                X += value
                current_command = ''
            elif current_command.startswith('noop'):
                current_command = ''
        cycle += 1

    return display


def main():
    with open('inputs/day10.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    assert part1(test_data) == 13140, f'Part 1 returned {part1(test_data)}'
    part1_result = part1(data)
    assert part1_result == 14240, f'Part 1 returned {part1_result}'

    part_example_solution = '##..##..##..##..##..##..##..##..##..##..###...###...###...###...###...###...###.####....####....####....####....####....#####.....#####.....#####.....#####.....######......######......######......###########.......#######.......#######.....'
    assert part2(test_data) == part_example_solution, f'Part 2 returned {part2(test_data)}'
    part2_result = part2(data)
    assert part2_result == '###..#....#..#.#....#..#.###..####.#..#.#..#.#....#..#.#....#.#..#..#....#.#..#.#..#.#....#..#.#....##...###....#..####.###..#....#..#.#....#.#..#..#..#...#..#.#....#....#..#.#....#.#..#..#.#....#..#.#....####..##..####.#..#.###..####.#..#.', f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
