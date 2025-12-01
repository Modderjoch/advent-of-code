import os

current_dir = os.getcwd()

parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, 'advent-of-code/Input/day1.txt')

lines = []
total_zero = 0
total_sum = 50

a = 0
b = 100

with open (file_path, 'r') as file:
    lines = file.readlines()

for i, item in enumerate(lines):
    lines[i] = lines[i].replace("R", "+").replace("L", "-")
    lines[i] = int(lines[i])

    total_sum += lines[i]

    wrap_total = ((total_sum - a) % (b - a) + a)

    print("The dial is rotated [" + str(lines[i]) + "] to point at [" + str(wrap_total) + "].")

    if(wrap_total == 0):
        total_zero += 1

print("The dial points at [" + str(a) + "] a total of [" + str(total_zero) + "] times during this process")