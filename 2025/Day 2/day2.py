import os

current_dir = os.getcwd()

parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, 'advent-of-code/Input/day2.txt')

ranges = []
sum_of_invalid_ids = 0
invalid_ids = []
puzzle = 0

def find_divisors(number):
    divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            if(i != number):
                divisors.append(i)
    return divisors

def split_string_for_loop(id, divisor):

    parts = [id[i:i+divisor] for i in range(0, len(id), divisor)]
    result = len(set(parts)) == 1

    print(str(parts) + " " + str(result))
    return result

with open (file_path, 'r') as file:
    data = file.readline()
    ranges = data.split(",")
    
    ranges = list(filter(lambda x: not x.startswith("0"), ranges))

    puzzle = input("Enter the solution you want to receive. 1 or 2")

for i, id_range in enumerate(ranges):
    ids = id_range.split("-")

    first_id = int(ids[0])
    last_id = int(ids[1])

    for k in range(first_id, last_id + 1):

        l = str(k)

        if(puzzle == "1"):
            
            midpoint = len(l) // 2
            first_half = l[:midpoint]
            second_half = l[midpoint:]

            if(first_half == second_half):
                print("Invalid ID found " + first_half + second_half)
                sum_of_invalid_ids += k
        
        elif(puzzle == "2"):
            divisors = find_divisors(len(l))
            for d, divisor in enumerate(divisors):
                if(split_string_for_loop(l, divisor)):
                    print("Invalid ID found " + l)
                    
                    if(l in invalid_ids):
                        continue
                    else:
                        invalid_ids.append(l)
                        sum_of_invalid_ids += k
        
print("Total of invalid IDs: " + str(sum_of_invalid_ids))