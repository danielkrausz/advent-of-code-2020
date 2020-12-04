import os
import re

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'day04.txt')

    field_rules = {'byr': r"(19[2-9|0]\d)|(200[0-2])",
                   'iyr': r"(20((1\d)|(20)))",
                   'eyr': r"(20((2\d)|(30)))",
                   'hgt': r"(((1[5-8]\d)|(19[0-3]))cm)|(((59)|(6\d)|(7[0-6]))in)",
                   'hcl': r"#(\d|[a-f]){6}",
                   'ecl': r"(amb|blu|brn|gry|grn|hzl|oth)", 
                   'pid': r"^(\d{9})$"}

    with open(filename) as f:
        data_array = f.read().split(os.linesep + os.linesep)
        part1 = 0
        part2 = 0
        for data in data_array:
            fields_valid = False
            if all(x in data for x in field_rules.keys()):
                fields_valid = True
                part1 += 1
                fields_dict = dict(x.split(":")
                                   for x in re.split(' |\n', data))
                for k, v in fields_dict.items():
                    rule = str(field_rules.get(k))
                    if k != 'cid' and re.match(rule, v) is None:
                        fields_valid = False
                        break
            if fields_valid:
                part2 += 1

        print(f"{part1=}")
        print(f"{part2=}")
