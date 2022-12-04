import sys

sys.path.append("..")
import utils

# Day 3: Rucksack Reorganization

data = utils.read_str_list()

score = 0
for i in range(0, len(data), 3):
    duplicate: str = list(set(data[i]).intersection(set(data[i+1])).intersection(set(data[i+2])))[0]
    if duplicate.islower():
        score += ord(duplicate) - 96
    else:
        score += ord(duplicate) - 38

print('Sum of priorities:', score)
