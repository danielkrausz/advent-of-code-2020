import os
import sys

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'day03.txt')

    slopes = [
        {'D': 1, 'R': 1},
        {'D': 1, 'R': 3},  # Part 1
        {'D': 1, 'R': 5},
        {'D': 1, 'R': 7},
        {'D': 2, 'R': 1},
    ]

    with open(filename) as f:
        map = f.read().splitlines()
        width = len(map[0]) - 1
        height = len(map)

        tree_mult = 1

        for slope in slopes:
            i = j = 0
            tree_cnt = 0
            while (i < height):
                if (map[i][j] == '#'):
                    tree_cnt += 1

                i += slope['D']

                if (j + slope['R']) > width:
                    j = slope['R'] - (width - j) - 1
                else:
                    j += slope['R']

            tree_mult *= tree_cnt

            if slope == {'D': 1, 'R': 3}:
                print(f"Part 1: {slope=}: {tree_cnt}")  # Part 1

        print(f"Part 2: {tree_mult}")  # Part 2
