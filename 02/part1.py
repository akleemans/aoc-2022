import sys

sys.path.append("..")
import utils

# Day 2: Rock Paper Scissors

data = utils.read_str_matrix()
score = 0
shape_values = {'X': 1, 'Y': 2, 'Z': 3}

for game in data:
    opponent_shape, my_shape = game
    score += shape_values[my_shape]
    pairing = opponent_shape + my_shape

    if pairing in ['AX', 'BY', 'CZ']:
        score += 3
    elif pairing in ['CX', 'AY', 'BZ']:
        score += 6

print('Score:', score)
