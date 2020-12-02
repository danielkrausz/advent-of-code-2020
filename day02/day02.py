import os
import re

# Part 1
def pass_is_valid(lowest, highest, letter, passw):
    letter_cnt = passw.count(letter)
    return letter_cnt >= lowest and letter_cnt <= highest

# Part 2 
def pass_is_valid_2(pos1, pos2, letter, passw):
    a = passw[pos1-1] == letter
    b = passw[pos2-1] == letter
    return (a and not b) or (not a and b)

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'day02.txt')
    valid_cnt_1 = 0
    valid_cnt_2 = 0

    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip(' \t\n\r').split(' ')
            lowest, highest = [int(n) for n in line[0].split('-')]
            if pass_is_valid(lowest, highest, line[1][0], line[2]):
                valid_cnt_1 += 1 
            if pass_is_valid_2(lowest, highest, line[1][0], line[2]):
                valid_cnt_2 += 1

    print(f"{valid_cnt_1=}")
    print(f"{valid_cnt_2=}")