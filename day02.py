from typing import List

# Day 2: Rock Paper Scissors

test_data = '''A Y
B X
C Z'''.split('\n')


def part1(data: List[str]):
    score = 0
    shape_values = {'X': 1, 'Y': 2, 'Z': 3}

    for game in data:
        opponent_shape, my_shape = game.split(' ')
        score += shape_values[my_shape]
        pairing = opponent_shape + my_shape

        if pairing in ['AX', 'BY', 'CZ']:
            score += 3
        elif pairing in ['CX', 'AY', 'BZ']:
            score += 6
    return score


def part2(data: List[str]):
    score = 0
    shape_values = {'A': 1, 'B': 2, 'C': 3}
    lose_against = {'A': 'C', 'B': 'A', 'C': 'B'}
    win_against = {'A': 'B', 'B': 'C', 'C': 'A'}

    for game in data:
        opponent_shape, outcome = game.split(' ')
        if outcome == 'X':  # lose
            my_shape = lose_against[opponent_shape]
        elif outcome == 'Y':  # draw
            my_shape = opponent_shape
        else:  # win
            my_shape = win_against[opponent_shape]

        score += shape_values[my_shape]
        pairing = opponent_shape + my_shape

        if pairing in ['AA', 'BB', 'CC']:
            score += 3
        elif pairing in ['CA', 'AB', 'BC']:
            score += 6
    return score


def main():
    with open('inputs/day02.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 15, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 10624, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 12, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 14060, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
