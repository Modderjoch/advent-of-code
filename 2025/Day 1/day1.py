import os
import math

current_dir = os.getcwd()

parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, 'advent-of-code/Input/day1_example.txt')

lines = []
total_zero_at_end_rotation = 0
total_zero_during_rotation = 0
total_sum = 50
wrap_total = 50

a = 0
b = 100

def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False
    
def is_divisible_by_hundred(number):
    if number%100 == 0:
        return True
    else:
        return False

with open (file_path, 'r') as file:
    lines = file.readlines()

for i, item in enumerate(lines):
    lines[i] = lines[i].replace("R", "+").replace("L", "-")
    lines[i] = int(lines[i])

    print("Rotated from " + str(wrap_total) + " to " + str(wrap_total + lines[i]))

    # PART TWO

    if(wrap_total + lines[i] < 0 and wrap_total != 0 or wrap_total + lines[i] > 100 and wrap_total != 0 or abs(lines[i]) > 100):
        if(abs(lines[i]) > 100):
            total_zero_during_rotation += math.floor((wrap_total + abs(lines[i])) / 100)
            if(wrap_total == 0 and is_even(abs(lines[i])) or is_even(wrap_total + lines[i]) and is_divisible_by_hundred(wrap_total + lines[i])):
                total_zero_during_rotation -= 1
            print("Extra rotations due to more than 100 > " + str(math.floor((wrap_total + abs(lines[i])) / 100)))
        else:
            total_zero_during_rotation += 1
            print("Rotation past [0]")

    # PART ONE

    total_sum += lines[i]
    
    wrap_total = ((total_sum - a) % (b - a) + a)

    print("The dial is rotated [" + str(lines[i]) + "] to point at [" + str(wrap_total) + "].")

    if(wrap_total == 0):
        total_zero_at_end_rotation += 1

    total_zero = total_zero_at_end_rotation + total_zero_during_rotation

print("The dial points at [" + str(a) + "] a total of [" + str(total_zero_at_end_rotation) + "] times at the end of a rotation, plus [" + str(total_zero_during_rotation) + "] more times during a rotation." 
      + " The password is [" + str(total_zero) + "].")