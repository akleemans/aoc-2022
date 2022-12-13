import math

# Day 12: Hill Climbing Algorithm

test_data = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''.split('\n')


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def is_reachable(a: str, b: str) -> bool:
    a = a.replace('S', 'a').replace('E', 'z')
    b = b.replace('S', 'a').replace('E', 'z')
    diff = ord(b) - ord(a)
    return diff <= 1


def add_nodes(pos, grid, distances):
    l = []
    candidates = [add(pos, o) for o in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    for c in candidates:
        # Outside grid
        if c[0] < 0 or c[1] < 0 or c[0] >= len(grid) or c[1] >= len(grid[0]):
            continue
        # Target has already same or lower distance
        if distances[c[0]][c[1]] <= distances[pos[0]][pos[1]] - 1:
            continue
        # Target not reachable
        if not is_reachable(grid[pos[0]][pos[1]], grid[c[0]][c[1]]):
            continue
        l.append(c)
    return l


def search_letter(s: str, data):
    pos = (0, 0)
    for y in range(len(data)):
        if s in data[y]:
            x = data[y].index(s)
            pos = (y, x)
    return pos


def search_all_letters(s: str, data):
    positions = []
    for y in range(len(data)):
        if s in data[y]:
            x = data[y].index(s)
            positions.append((y, x))
    return positions


def part1(data):
    w = len(data[0])
    h = len(data)

    # Search start
    start = search_letter('S', data)
    end = search_letter('E', data)
    # print('Start:', start, 'end:', end)

    distances = [[math.inf for x in range(w)] for y in range(h)]
    queue = [(start, 0)]
    round = 0
    while len(queue) > 0:
        round += 1
        pos, distance = queue.pop(0)
        # Check if entry is a viable
        if distance >= distances[pos[0]][pos[1]]:
            continue
        distances[pos[0]][pos[1]] = distance
        # print('Initial distance:', distances[pos[0]][pos[1]])
        queue.extend([((n[0], n[1]), distance + 1) for n in add_nodes(pos, data, distances)])
        # if round % 10000 == 0:
        #    print('Queue length:', len(queue))

    # print('Took', round, 'rounds')
    return distances[end[0]][end[1]]


def part2(data):
    w = len(data[0])
    h = len(data)

    # Search start
    end = search_letter('E', data)
    starts = search_all_letters('a', data)
    shortest_path_candidates = []

    for start in starts:
        distances = [[math.inf for x in range(w)] for y in range(h)]
        queue = [(start, 0)]
        while len(queue) > 0:
            pos, distance = queue.pop(0)
            # Check if entry is a viable
            if distance >= distances[pos[0]][pos[1]]:
                continue
            distances[pos[0]][pos[1]] = distance
            queue.extend([((n[0], n[1]), distance + 1) for n in add_nodes(pos, data, distances)])
            shortest_path_candidates.append(distances[end[0]][end[1]])
    return min(shortest_path_candidates)


def main():
    with open('inputs/day12.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 31, f'Part 1 returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 330, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 29, f'Part 2 returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 321, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
