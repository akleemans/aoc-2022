import sys

sys.path.append("..")
import utils

# Day 2: Rock Paper Scissors

data = utils.read_str_matrix()
score = 0
shape_values = {'A': 1, 'B': 2, 'C': 3}
lose_against = {'A': 'C', 'B': 'A', 'C': 'B'}
win_against = {'A': 'B', 'B': 'C', 'C': 'A'}

for game in data:
    opponent_shape, outcome = game
    if outcome == 'X':  # lose
        my_shape = lose_against[opponent_shape]
    elif outcome == 'Y':  # draw
        my_shape = opponent_shape
    else:  # win
        my_shape = win_against[opponent_shape]

    score += shape_values[my_shape]
    pairing = opponent_shape + my_shape

    if pairing in ['AA', 'BB', 'CC']:
        score += 3
    elif pairing in ['CA', 'AB', 'BC']:
        score += 6

print('Score:', score)
