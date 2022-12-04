import sys

sys.path.append("..")
import utils


# Day 4: Camp Cleanup

def have_overlap(a1: int, a2: int, b1: int, b2: int) -> bool:
    """Determine if two ranges a1-a2, b1-b2 have an overlap"""
    return a1 <= b1 <= a2 or b1 <= a1 <= b2


def main():
    data = utils.read_str_list()

    score = 0

    for line in data:
        a, b = line.split(',')
        a1, a2 = [int(x) for x in a.split('-')]
        b1, b2 = [int(x) for x in b.split('-')]
        if have_overlap(a1, a2, b1, b2):
            score += 1

    print('Fully contained ranges:', score)


if __name__ == '__main__':
    main()
