from typing import List, Tuple

# Day 22: Monkey Map

test_data = '''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5'''.split('\n')

# Global attributes
height = 0
width = 0
stitchings = {}


class Node:
    def __init__(self, idx: int, x: int, y: int, is_wall: bool):
        self.idx = idx
        self.x = x
        self.y = y
        self.is_wall = is_wall
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.direction_modifiers = {}

    def move(self, direction: str):
        node = {'U': self.up, 'D': self.down, 'L': self.left, 'R': self.right}[direction]
        if direction in self.direction_modifiers:
            direction = self.direction_modifiers[direction]
        return node, direction

    def __str__(self):
        return f'N{self.x, self.y}'

    def __repr__(self):
        return self.__str__()


def parse_input(data) -> Tuple[List[Node], List[str]]:
    global height
    global width
    instr_str = data[-1]
    instr = []
    current_instr = ''
    for c in instr_str:
        if c in ['R', 'L']:
            instr.append(current_instr)
            instr.append(c)
            current_instr = ''
        else:
            current_instr += c
    if current_instr != '':
        instr.append(current_instr)

    is_wall = {'#': True, '.': False}
    height = len(data[:-2])
    width = len(data[0])

    # Create nodes
    nodes = []
    for y in range(height):
        line = data[y]
        for x in range(width):
            if x >= len(line):
                nodes.append(None)
                continue
            c = line[x]
            if c == ' ':
                nodes.append(None)
            else:
                idx = y * width + x
                nodes.append(Node(idx, x, y, is_wall[c]))

    return nodes, instr


def move(node: Node, facing: str, instr: str) -> Tuple[Node, str]:
    change_direction = {
        'U': {'L': 'L', 'R': 'R'}, 'D': {'L': 'R', 'R': 'L'},
        'L': {'L': 'D', 'R': 'U'}, 'R': {'L': 'U', 'R': 'D'},
    }
    if instr in ['L', 'R']:
        new_facing = change_direction[facing][instr]
        # print(f'Move: Changing direction from {facing} to {new_facing}')
        return node, new_facing
    else:
        dist = int(instr)
        # print(f'Move: Starting to move {dist} in direction {facing}')
        for i in range(dist):
            # Try to move as far as possible
            next_node, new_facing = node.move(facing)
            if next_node.is_wall:
                break
            node = next_node
            facing = new_facing
        # print(f'Move: Moved {facing} to {node}')
        return node, facing


def solve(start_node: Node, instructions: List[str]) -> Tuple[Node, str]:
    facing = 'R'
    node = start_node
    for instr in instructions:
        node, facing = move(node, facing, instr)
    return node, facing


def get_idx(x: int, y: int) -> int:
    return y * width + x


def link_nodes(nodes: List[Node]) -> None:
    """ Create neighborship relations among nodes """

    def get_next_node(node: Node, direction: str):
        diff = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
        x = node.x
        y = node.y
        candidate = None
        while candidate is None:
            x = (x + diff[direction][0]) % width
            y = (y + diff[direction][1]) % height
            candidate = nodes[get_idx(x, y)]
        return candidate

    for node in [n for n in nodes if n is not None]:
        node.up = get_next_node(node, 'U')
        node.down = get_next_node(node, 'D')
        node.left = get_next_node(node, 'L')
        node.right = get_next_node(node, 'R')
        # print(f'Linked neighbors for {node}: U: {node.up}, D: {node.down}, L: {node.left}, R: {node.right}')
        # input()


def part1(data: List[str]):
    nodes, instr = parse_input(data)
    link_nodes(nodes)
    start_node = next(n for n in nodes if n is not None)
    node, facing = solve(start_node, instr)

    # print('Solution: Row:', node.y, 'col:', node.x, 'facing:', facing)
    pw = 1000 * (node.y + 1) + 4 * (node.x + 1) + {'R': 0, 'D': 1, 'L': 2, 'U': 3}[facing]
    return pw


def link_nodes_pt2(nodes: List[Node]) -> None:
    def get_next_node(node: Node, direction: str) -> Node:
        stitching_pair = (node.x, node.y, direction)
        if stitching_pair in stitchings:
            x, y = stitchings[stitching_pair]
            return nodes[get_idx(x, y)]

        # Normal case
        diff = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

        x = node.x + diff[direction][0]
        y = node.y + diff[direction][1]
        return nodes[get_idx(x, y)]

    for node in [n for n in nodes if n is not None]:
        node.up = get_next_node(node, 'U')
        node.down = get_next_node(node, 'D')
        node.left = get_next_node(node, 'L')
        node.right = get_next_node(node, 'R')
        # print(f'Linked neighbors for {node}: U: {node.up}, D: {node.down}, L: {node.left}, R: {node.right}')
        # input()


def prepare_stitchings(nodes: List[Node]):
    """Manual stitching for input layout"""
    # A up -> F down
    for i in range(50):
        stitchings[(i + 100, 0, 'U')] = (i, 199)

    # A right -> D right
    for i in range(50):
        stitchings[(149, i, 'R')] = (99, 149 - i)
        nodes[get_idx(149, i)].direction_modifiers['R'] = 'L'

    # A down -> C right
    for i in range(50):
        stitchings[(100 + i, 49, 'D')] = (99, 50 + i)
        nodes[get_idx(100 + i, 49)].direction_modifiers['D'] = 'L'

    # B up -> F left
    for i in range(50):
        stitchings[(50 + i, 0, 'U')] = (0, 150 + i)
        nodes[get_idx(50 + i, 0)].direction_modifiers['U'] = 'R'

    # B left -> E right
    for i in range(50):
        stitchings[(50, i, 'L')] = (0, 149 - i)
        nodes[get_idx(50, i)].direction_modifiers['L'] = 'R'

    # C left -> E up
    for i in range(50):
        stitchings[(50, 50 + i, 'L')] = (i, 100)
        nodes[get_idx(50, 50 + i, )].direction_modifiers['L'] = 'D'

    # C right -> A down
    for i in range(50):
        stitchings[(99, 50 + i, 'R')] = (100 + i, 49)
        nodes[get_idx(99, 50 + i)].direction_modifiers['R'] = 'U'

    # D right -> A right
    for i in range(50):
        stitchings[(99, 100 + i, 'R')] = (149, 49 - i)
        nodes[get_idx(99, 100 + i)].direction_modifiers['R'] = 'L'

    # D down -> F right
    for i in range(50):
        stitchings[(50 + i, 149, 'D')] = (49, 150 + i)
        nodes[get_idx(50 + i, 149)].direction_modifiers['D'] = 'L'

    # E up -> C left
    for i in range(50):
        stitchings[(i, 100, 'U')] = (50, 50 + i)
        nodes[get_idx(i, 100)].direction_modifiers['U'] = 'R'

    # E left -> B left
    for i in range(50):
        stitchings[(0, 100 + i, 'L')] = (50, 49 - i)
        nodes[get_idx(0, 100 + i)].direction_modifiers['L'] = 'R'

    # F left -> B up
    for i in range(50):
        stitchings[(0, 150 + i, 'L')] = (50 + i, 0)
        nodes[get_idx(0, 150 + i)].direction_modifiers['L'] = 'D'

    # F down -> A up
    for i in range(50):
        stitchings[(i, 199, 'D')] = (100 + i, 0)

    # F right -> D down
    for i in range(50):
        stitchings[(49, 150 + i, 'R')] = (50 + i, 149)
        nodes[get_idx(49, 150 + i)].direction_modifiers['R'] = 'U'


def part2(data: List[str]):
    nodes, instr = parse_input(data)
    prepare_stitchings(nodes)
    link_nodes_pt2(nodes)
    for node in [n for n in nodes if n is not None]:
        if node.left is None or node.right is None or node.up is None or node.down is None:
            print('Faulty node configuration! for node:', node, 'x:', node.x, 'y:', node.y)
            return

    start_node = next(n for n in nodes if n is not None)
    node, facing = solve(start_node, instr)

    # print('Solution: Row:', node.y, 'col:', node.x, 'facing:', facing)
    pw = 1000 * (node.y + 1) + 4 * (node.x + 1) + {'R': 0, 'D': 1, 'L': 2, 'U': 3}[facing]

    return pw


def main():
    with open('inputs/day22.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 6032, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 57350, f'Part 1 returned {part1_result}'

    # part2_test_result = part2(test_data)
    # assert part2_test_result == 5031, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 104385, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
