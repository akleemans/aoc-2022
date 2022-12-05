import sys
from typing import List

sys.path.append("..")
import utils


# Day 5: Supply Stacks

def index_of_first(l: List[str], predicate):
    for i, v in enumerate(l):
        if predicate(v):
            return i


def prepare_stack(data: List[str]) -> List[List[str]]:
    # First, find index
    bottom_line = index_of_first(data, lambda x: x.startswith(' 1'))

    # Initialize stacks
    amount_of_stacks = int(data[bottom_line].split(' ')[-1])
    stacks = [[] for _ in range(amount_of_stacks)]
    positions = []

    # Collect positions
    for i in range(len(data[bottom_line])):
        if data[bottom_line][i] != ' ':
            positions.append(i)

    for line_nr in range(bottom_line - 1, -1, -1):
        for x in range(len(positions)):
            if len(data[line_nr]) < positions[x]:
                continue
            n = data[line_nr][positions[x]]
            if n != ' ':
                stacks[x].append(n)
    return stacks


####

data = utils.read_str_list('input.txt')

stacks = prepare_stack(data)

# Prepare instruction
instructions = []
flag = False
for line in data:
    if line.startswith('move'):
        flag = True
    if flag:
        instructions.append(line)

# Execute instructions
for instruction in instructions:
    parts = instruction.split(' ')
    amount, source, target = int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1

    for i in range(amount):
        crate = stacks[source].pop()
        stacks[target].append(crate)

print('Top of stack:', ''.join([x[-1] for x in stacks]))
