import os
import sys

def part1(input_array):
    sum_2020 = 2020
    for num in input_array:
        if sum_2020-num in input_array:
            A = num
            B = sum_2020-num
            return A*B
    return 0
    

def part2(input_array):
    sum_2020 = 2020
    for i in range(len(input_array)):
        for j in range(i, len(input_array)-1):
            if (sum_2020-input_array[i]-input_array[j]) in input_array:
                A=input_array[i]
                B=input_array[j]
                C=sum_2020-input_array[i]-input_array[j]
                return A*B*C
    return 0


if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'day01.txt')
    input_array = []
    with open(filename) as f:
        input_array = [int(x) for x in f]

    print(part1(input_array))
    print(part2(input_array))