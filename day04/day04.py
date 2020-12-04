import os
import re

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'day04.txt')

    req_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    field_rules = {'byr': r"(19[2-9|0][0-9])|(200[1-2])",
                   'iyr': r"(20(1[0-9])|(20))",
                   'eyr': r"(20(2[0-9])|(30))",
                   'hgt': r"(((1[5-8][0-9])|(19[0-3]))cm)|(((59)|(6[0-9])|(7[0-6]))in)",
                   'hcl': r"#([0-9]|[a-f]){6}",
                   'ecl': r"(amb|blu|brn|gry|grn|hzl|oth)", 
                   'pid': r"^(\d{9})$"}

    with open(filename) as f:
        data_array = f.read().split(os.linesep + os.linesep)
        part1 = 0
        part2 = 0
        for data in data_array:
            fields_valid = False
            if all(x in data for x in req_fields):
                fields_valid = True
                part1 += 1
                fields_dict = dict(x.split(":")
                                   for x in re.split(' |\n', data))
                for k, v in fields_dict.items():
                    rule = str(field_rules.get(k))
                    if k != 'cid' and re.search(rule, v) is None:
                        fields_valid = False
                        break

            if fields_valid:
                part2 += 1

        print(part1)
        print(part2)
