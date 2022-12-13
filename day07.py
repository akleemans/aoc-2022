from typing import List

# Day 7: No Space Left On Device

test_data = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''.split('\n')


class Node:
    def __init__(self, name: str, size: int, parent):
        self.children = []
        self.level = 0
        self.name = name
        self.size = size
        self.parent = parent
        if parent is not None:
            self.level = parent.level + 1

    def get_child(self, name: str):
        # print('Searching', self.children, 'for', name)
        node = next(filter(lambda n: n.name == name, self.children), None)
        if node is None:
            raise FileNotFoundError('Child not found: ' + name)
        return node

    def add_child(self, name, size):
        self.children.append(Node(name, size, self))

    def get_directories(self):
        # print('Walking', self)
        l = [self]
        for c in self.children:
            if len(c.children) > 0:
                l.extend(c.get_directories())
        return l

    def __str__(self):
        return self.name + '(' + str(self.level) + ')'

    def __repr__(self):
        return self.__str__()


def part1(data: List[str]):
    root = Node("/", 0, None)
    current_node = root

    for line in data[1:]:
        # print('> Processing command:', line)
        if line.startswith('$ cd'):
            if line == '$ cd ..':
                # print('Moving up from', current_node)
                current_node = current_node.parent
            else:
                name = line.split(' ')[2]
                # print('Moving down to', name, 'level:', current_node.level)
                current_node = current_node.get_child(name)
        elif not line.startswith('$'):
            if line.startswith('dir'):
                name = line.split(' ')[1]
                # print('Creating directory', name)
                current_node.add_child(name, 0)
            else:
                size, name = line.split(" ")
                # print('Creating file', name)
                size = int(size)
                current_node.add_child(name, size)
                n = current_node
                while True:
                    n.size += size
                    n = n.parent
                    if n is None:
                        break
    # print('Root size:', root.size)
    # Find small directories
    small_directories = [d for d in root.get_directories() if d.size <= 100000]
    return sum([d.size for d in small_directories])


def part2(data: List[str]):
    # name, size, children
    root = Node("/", 0, None)
    current_node = root

    for line in data[1:]:
        # print('> Processing command:', line)
        if line.startswith('$ cd'):
            if line == '$ cd ..':
                # print('Moving up from', current_node)
                current_node = current_node.parent
            else:
                name = line.split(' ')[2]
                # print('Moving down to', name, 'level:', current_node.level)
                current_node = current_node.get_child(name)
        elif not line.startswith('$'):
            if line.startswith('dir'):
                name = line.split(' ')[1]
                # print('Creating directory', name)
                current_node.add_child(name, 0)
            else:
                size, name = line.split(" ")
                # print('Creating file', name)
                size = int(size)
                current_node.add_child(name, size)
                n = current_node
                while True:
                    n.size += size
                    n = n.parent
                    if n is None:
                        break

    # print('Root size:', root.size)
    target_size = root.size - 40000000
    # print('target_size:', target_size)

    possible_directories = [d for d in root.get_directories() if d.size >= target_size]
    # print('possible_directories:', [d.size for d in possible_directories])

    # Smallest directory to free up enough space
    return min([d.size for d in possible_directories])


def main():
    with open('inputs/day07.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 95437, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 2031851, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 24933642, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 2568781, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
