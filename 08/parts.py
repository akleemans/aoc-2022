from typing import List

# Day 8: Treetop Tree House

test_data = '''30373
25512
65332
33549
35390'''.split('\n')


def is_visible(i, j, data):
    w = len(data[0])
    h = len(data)

    max_height = int(data[i][j]) - 1

    # up
    visible = True
    for a in range(i - 1, -1, -1):
        if int(data[a][j]) > max_height:
            visible = False
    if visible: return True

    # down
    visible = True
    for a in range(i + 1, h, 1):
        if int(data[a][j]) > max_height:
            visible = False
    if visible: return True

    # left
    visible = True
    for b in range(j - 1, -1, -1):
        if int(data[i][b]) > max_height:
            visible = False
    if visible: return True

    # right
    visible = True
    for b in range(j + 1, w, 1):
        if int(data[i][b]) > max_height:
            visible = False

    return visible


def scenic_score(i, j, data):
    w = len(data[0])
    h = len(data)

    max_height = int(data[i][j]) - 1

    # up
    scores = [0, 0, 0, 0]
    for a in range(i - 1, -1, -1):
        scores[0] += 1
        if int(data[a][j]) > max_height:
            break

    # down
    for a in range(i + 1, h, 1):
        scores[1] += 1
        if int(data[a][j]) > max_height:
            break

    # left
    for b in range(j - 1, -1, -1):
        scores[2] += 1
        if int(data[i][b]) > max_height:
            break

    # right
    for b in range(j + 1, w, 1):
        scores[3] += 1
        if int(data[i][b]) > max_height:
            break

    return scores[0] * scores[1] * scores[2] * scores[3]


def part1(data: List[str]):
    w = len(data[0])
    h = len(data)

    score = 2 * (w - 1) + 2 * (h - 1)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if is_visible(i, j, data):
                score += 1
    return score


def part2(data: List[str]):
    w = len(data[0])
    h = len(data)

    highest_score = 0
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            highest_score = max(highest_score, scenic_score(i, j, data))
    return highest_score


if __name__ == '__main__':
    with open('input.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    assert part1(test_data) == 21, f'Part 1 returned {part1(test_data)}'
    print('Part 1:', part1(data))

    assert part2(test_data) == 8, f'Part 2 returned {part2(test_data)}'
    print('Part 2:', part2(data))
