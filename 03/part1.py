import sys

sys.path.append("..")
import utils

# Day 3: Rucksack Reorganization

data = utils.read_str_list()

score = 0
for rucksack in data:
    l = int(len(rucksack) / 2)
    comp1 = rucksack[:l]
    comp2 = rucksack[l:]
    duplicate: str = list(set(comp1).intersection(set(comp2)))[0]
    if duplicate.islower():
        score += ord(duplicate) - 96
    else:
        score += ord(duplicate) - 38

print('Sum of priorities:', score)
