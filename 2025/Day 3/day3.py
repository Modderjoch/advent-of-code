import os

current_dir = os.getcwd()

parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, 'advent-of-code/Input/day2.txt')

with open (file_path, 'r') as file:
    input = file.readline()
    ranges = input.split(",")
    
    ranges = list(filter(lambda x: not x.startswith("0"), ranges))