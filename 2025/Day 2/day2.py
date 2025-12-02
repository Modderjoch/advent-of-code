import os

current_dir = os.getcwd()

parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, 'advent-of-code/Input/day2_example.txt')

ranges = []
sum_of_invalid_ids = 0

with open (file_path, 'r') as file:
    input = file.readline()
    ranges = input.split(",")
    
    ranges = list(filter(lambda x: not x.startswith("0"), ranges))

    print(ranges)

for i, id_range in enumerate(ranges):
    ids = id_range.split("-")

    first_id = int(ids[0])
    last_id = int(ids[1])

    for k in range(first_id, last_id + 1):

        l = str(k)

        midpoint = len(l) // 2
        first_half = l[:midpoint]
        second_half = l[midpoint:]

        if(first_half == second_half):
            print("Invalid ID found " + first_half + second_half)
            sum_of_invalid_ids += k
        
print("Total of invalid IDs: " + str(sum_of_invalid_ids))