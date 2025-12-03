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

    puzzle = input("Enter the solution you want to see.\n\n 1 or 2 \n\n")

for i, bank in enumerate(banks):

    batteries = [bank[i:i+1] for i in range(0, len(bank), 1)]

    if(puzzle == "1"):
        largest_battery = max(batteries[:-1])

        largest_battery_index = batteries.index(largest_battery) + 1

        new_batteries = batteries[largest_battery_index:]

        second_largest_battery = max(new_batteries)

        largest_possible_joltage = int(str(largest_battery) + str(second_largest_battery))

        total_output_joltage += largest_possible_joltage
        
    elif(puzzle == "2"):

        largest_battery = max(batteries[:-11])

        largest_battery_index = batteries.index(largest_battery) + 1

        new_batteries = batteries[largest_battery_index:]

        batteries_to_remove = len(new_batteries) - 11

        for b in range(0, batteries_to_remove, 1):
            lowest_battery = min(new_batteries)

            lowest_battery_index = new_batteries.index(lowest_battery)

            new_batteries.pop(lowest_battery_index)

        largest_possible_joltage = largest_battery + "".join(new_batteries)

        largest_joltage_int = int(largest_possible_joltage)

        total_output_joltage += largest_joltage_int

print("The total output joltage is " + str(total_output_joltage))

# 169666831865734 is too low
# 
# 1695089027034985 is too high