import sys

sys.path.append("..")
import utils

# Day 6: Tuning Trouble

line = utils.read_str_list('input.txt')[0]

for i in range(4, len(line), 1):
    last_four = line[i - 4:i]
    if len(last_four) == len(set(last_four)):
        print('Solution:', i)
        break
