import os

current_dir = os.getcwd()

parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, 'advent-of-code/Input/day3_example.txt')

banks = []
total_output_joltage = 0
battery_count = 12

with open (file_path, 'r') as file:
    banks = file.readlines()

    for i, bank in enumerate(banks):
        banks[i] = bank.replace("\n", "")

    puzzle = input("Enter the solution you want to see.\n\n 1 or 2 \n\n")

for i, bank in enumerate(banks):

    batteries = [int(bank[i:i+1]) for i in range(len(bank))]

    if(puzzle == "1"):
        largest_battery = max(batteries[:-1])

        largest_battery_index = batteries.index(largest_battery) + 1

        new_batteries = batteries[largest_battery_index:]

        second_largest_battery = max(new_batteries)

        largest_possible_joltage = int(str(largest_battery) + str(second_largest_battery))

        total_output_joltage += largest_possible_joltage
        
    elif(puzzle == "2"):

        new_batteries = batteries[:]

        biggest_battery = []

        for k in range(battery_count, 0, -1):

            largest_battery = max(new_batteries[:-k])

            # print(f"Largest battery found: {largest_battery}")

            largest_battery_index = new_batteries.index(largest_battery) + 1

            # print(largest_battery_index)

            new_batteries = new_batteries[largest_battery_index:]

            biggest_battery.append(largest_battery)

        largest_possible_joltage = "".join(str(b) for b in biggest_battery)

        largest_joltage_int = int(largest_possible_joltage)

        total_output_joltage += largest_joltage_int

print("The total output joltage is " + str(total_output_joltage))

# 169666831865734 is too low
# 171389956243660 is incorrect
# 1695089027034985 is too high