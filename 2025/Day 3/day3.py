import os

current_dir = os.getcwd()

parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, 'advent-of-code/Input/day3.txt')

banks = []
total_output_joltage = 0

with open (file_path, 'r') as file:
    banks = file.readlines()

    for i, bank in enumerate(banks):
        banks[i] = bank.replace("\n", "")

    print(banks)

for i, battery in enumerate(banks):

    batteries = [battery[i:i+1] for i in range(0, len(battery), 1)]

    largest_battery = max(batteries[:-1])

    largest_battery_index = batteries.index(largest_battery) + 1

    new_batteries = batteries[largest_battery_index:]

    second_largest_battery = max(new_batteries)

    largest_possible_joltage = int(str(largest_battery) + str(second_largest_battery))

    total_output_joltage += largest_possible_joltage

print("The total output joltage is " + str(total_output_joltage))