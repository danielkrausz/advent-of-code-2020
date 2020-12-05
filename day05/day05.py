import os

def convert_to_num(rows, match_dict):
    binary = rows.replace(match_dict['0'], '0').replace(match_dict['1'], '1')
    return int(binary, base=2)

def get_my_id(seat_ids):
    i = 0
    while i < len(seat_ids):
        if (seat_ids[i+1] - seat_ids[i] == 2):
            return seat_ids[i]+1
        else:
            i+=1
        
if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'day05.txt')

    seat_ids = []

    with open(filename) as f:
        passes = f.read().split()
        for boarding_pass in passes:
            row = convert_to_num(boarding_pass[:7], {'0': 'F', '1': 'B'})
            col = convert_to_num(boarding_pass[7:], {'0': 'L', '1': 'R'})
            seat_id = row*8+col
            seat_ids.append(seat_id)
    
    print(max(seat_ids)) # Part 1
    print(get_my_id(sorted(seat_ids))) # Part 2

