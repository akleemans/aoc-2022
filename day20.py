from typing import List

# Day 20: Grove Positioning System

test_data = '''1
2
-3
3
-2
0
4'''.split('\n')

test_data2 = '''8
2
32
-41
6
29
-4
6
-8
8
-3
-8
3
-5
0
-1
2
1
10
-9'''.split('\n')


class Item:
    def __init__(self, idx: int, n: int):
        # Not sure if needed, if accessible via list
        self.idx = idx
        self.n = n
        self.left = None
        self.right = None

    def set_neighbors(self, left: 'Item', right: 'Item'):
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.n} ({self.left.n}<>{self.right.n})'

    def __repr__(self):
        return self.__str__()


def move(node, n, m):
    """Move n steps on node in direction, modulo m?!"""
    r = abs(n) % m

    for _ in range(r):
        if n < 0:
            node = node.left
        elif n > 0:
            node = node.right
    return node


def mix(all_items):
    # Move around (change references)
    for i in range(len(all_items)):
        item = all_items[i]
        if item.n == 0:
            continue

        # Remove item first
        item.left.right = item.right
        item.right.left = item.left
        target = move(item, item.n, len(all_items) - 1)

        # Embed number
        if item.n < 0:
            r = target
            l = target.left
            l.right = item
            target.left = item
            item.left = l
            item.right = r
        elif item.n > 0:
            a = target
            b = target.right
            target.right = item
            b.left = item
            item.left = a
            item.right = b
        # print(f'...got new neighbors {item.left} and {item.right}!')
        # input()


def init_list(data, key=1):
    all_items = []
    # Initialize list
    for i in range(len(data)):
        new_item = Item(i, int(data[i]) * key)
        all_items.append(new_item)

    # Set neighbours
    for i in range(1, len(data) - 1):
        all_items[i].set_neighbors(all_items[i - 1], all_items[i + 1])
    # Manually set first and last
    all_items[0].set_neighbors(all_items[-1], all_items[1])
    all_items[-1].set_neighbors(all_items[-2], all_items[0])
    return all_items


def part1(data: List[str]):
    all_items = init_list(data)
    zero_item = next(i for i in all_items if i.n == 0)
    mix(all_items)

    # Find 1000th, 2000th, 3000th item
    item = zero_item
    result = 0
    for _ in range(3):
        item = move(item, 1000, len(all_items))
        result += item.n
    # print('result:', result)
    return result


def part2(data: List[str]):
    all_items = init_list(data, 811589153)
    zero_item = next(i for i in all_items if i.n == 0)

    for i in range(10):
        mix(all_items)

    # Find 1000th, 2000th, 3000th item
    item = zero_item
    result = 0
    for _ in range(3):
        item = move(item, 1000, len(all_items))
        result += item.n
    return result


def main():
    with open('inputs/day20.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 3, f'Part 1 test input returned {part1_test_result}'
    # part1_test2_result = part1(test_data2)
    # assert part1_test2_result == 0, f'Part 1 test input 2 returned {part1_test2_result}'
    part1_result = part1(data)
    assert part1_result == 4151, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 1623178306, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 7848878698663, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
