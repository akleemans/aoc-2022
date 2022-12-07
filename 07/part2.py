import sys

from node import Node

sys.path.append("..")
import utils

# Day 7: No Space Left On Device

data = utils.read_str_list('input.txt')

# name, size, children
root = Node("/", 0, None)
current_node = root

for line in data[1:]:
    print('> Processing command:', line)
    if line.startswith('$ cd'):
        if line == '$ cd ..':
            print('Moving up from', current_node)
            current_node = current_node.parent
        else:
            name = line.split(' ')[2]
            print('Moving down to', name, 'level:', current_node.level)
            current_node = current_node.get_child(name)
    elif not line.startswith('$'):
        if line.startswith('dir'):
            name = line.split(' ')[1]
            print('Creating directory', name)
            current_node.add_child(name, 0)
        else:
            size, name = line.split(" ")
            print('Creating file', name)
            size = int(size)
            current_node.add_child(name, size)
            n = current_node
            while True:
                n.size += size
                n = n.parent
                if n is None:
                    break

print('Root size:', root.size)
target_size = root.size - 40000000
print('target_size:', target_size)

possible_directories = [d for d in root.get_directories() if d.size >= target_size]
print('possible_directories:', [d.size for d in possible_directories])

print('Smallest directory to free up enough space:', min([d.size for d in possible_directories]))
