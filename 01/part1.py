import sys

sys.path.append("..")
import utils

data = utils.read_str_list()

highest_count = 0
count = 0
for calories in data:
    if calories == '':
        if highest_count < count:
            highest_count = count
        count = 0
    else:
        count += int(calories)

print('Highest calories count:', highest_count)
