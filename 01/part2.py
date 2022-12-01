import sys

sys.path.append("..")
import utils

data = utils.read_str_list()

current_count = 0
counts = []
for calories in data:
    if calories == '':
        counts.append(current_count)
        current_count = 0
    else:
        current_count += int(calories)

counts.sort(reverse=True)
print('3 highest calories count:', sum(counts[:3]))
