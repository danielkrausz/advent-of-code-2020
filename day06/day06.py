import os
import string

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'day06.txt')

    with open(filename) as f:
        answers = f.read().split(os.linesep + os.linesep)
        part1 = 0
        part2 = 0
        for answer in answers: 
            # Part 1
            part1 += len(set(answer.replace('\n', '')))

            # Part 2
            person_answer = answer.split()
            answer_intersect = set(string.ascii_lowercase)
            
            for a in person_answer:
                answer_intersect = answer_intersect & set(a)

            part2 += len(answer_intersect) 

        print(part1)
        print(part2)
