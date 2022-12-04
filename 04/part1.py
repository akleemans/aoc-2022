import sys

sys.path.append("..")
import utils

# Day 4: Camp Cleanup

data = utils.read_str_list()

score = 0

for line in data:
    a, b = line.split(',')
    a1, a2 = [int(x) for x in a.split('-')]
    b1, b2 = [int(x) for x in b.split('-')]
    if (a1 >= b1 and a2 <= b2) or (a1 <= b1 and a2 >= b2):
        score += 1

print('Fully contained ranges:', score)
