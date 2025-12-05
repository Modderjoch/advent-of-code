import os

current_dir = os.getcwd()

parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, 'advent-of-code/Input/day4.txt')

shelves = []
accessible_rolls = 1
total_accessible_rolls = 0

def loop_through_shelves(shelves, debug):
	accessible = 0
	shelf_ind = []
	square_ind = []

	for i, shelf in enumerate(shelves):
		for k, square in enumerate(shelf):
			if square == "@":
				number_of_rolls_in_adjacent = 0

				if i - 1 >= 0 and shelves[i-1] is not None:
					if k - 1 >= 0 and shelves[i-1][k-1] is not None:
						if shelves[i-1][k-1] == "@":
							number_of_rolls_in_adjacent += 1
							if debug == "Y":
								print("Roll found to the top-left")

					if shelves[i-1][k] is not None:
						if shelves[i-1][k] == "@":
							number_of_rolls_in_adjacent += 1
							if debug == "Y":
								print("Roll found above")

					if k + 1 <= len(shelf) - 1 and shelves[i-1][k+1] is not None:
						if shelves[i-1][k+1] == "@":
							if debug == "Y":
								print("Roll found to the top-right")
							number_of_rolls_in_adjacent += 1

				if i >= 0 and shelves[i] is not None:
					if k - 1 >= 0 and shelves[i][k-1] is not None:
						if shelves[i][k-1] == "@":
							if debug == "Y":
								print("Roll found to the left")
							number_of_rolls_in_adjacent += 1

					if k + 1 <= len(shelf) - 1 and shelves[i][k+1] is not None:
						if shelves[i][k+1] == "@":
							if debug == "Y":
								print("Roll found to the right")
							number_of_rolls_in_adjacent += 1

				if i + 1 <= len(shelves) - 1 and shelves[i+1] is not None:
					if k - 1 >= 0 and shelves[i+1][k-1] is not None:
						if shelves[i+1][k-1] == "@":
							number_of_rolls_in_adjacent += 1
							if debug == "Y":
								print("Roll found to the bottom-left")

					if shelves[i+1][k] is not None:
						if shelves[i+1][k] == "@":
							number_of_rolls_in_adjacent += 1
							if debug == "Y":
								print("Roll found below")

					if k + 1 <= len(shelf) - 1 and shelves[i+1][k+1] is not None:
						if shelves[i+1][k+1] == "@":
							number_of_rolls_in_adjacent += 1
							if debug == "Y":
								print("Roll found to the bottom-right")

				if number_of_rolls_in_adjacent < 4:
					accessible += 1
					shelf_ind.append(i)
					square_ind.append(k)

				if debug == "Y":
					print(f"For square {k+1} on shelf {i+1}, there are {number_of_rolls_in_adjacent} rolls adjacent.")

	return accessible, shelf_ind, square_ind

with open (file_path, 'r') as file:
    shelves = file.readlines()

    for i in range(0, len(shelves), 1):
        shelves[i] = list(shelves[i])

        shelves[i] = [x.replace('\n', '') for x in shelves[i]]

        shelves[i] = [x for x in shelves[i] if x]


    puzzle = input("Enter the solution you want to see.\n\n 1 or 2 \n\n")
    debug = input("Do you want to see the debug? \n\n Y/n \n\n")

shelves_index =[]
square_index = []

if puzzle == "1":
	accessible_rolls, shelves_index, square_index = loop_through_shelves(shelves, debug)
	total_accessible_rolls += accessible_rolls

	for i in range(len(shelves_index)):
		shelves[shelves_index[i]][square_index[i]] = "X"

else:
	while accessible_rolls > 0:
		accessible_rolls, shelves_index, square_index = loop_through_shelves(shelves, debug)
		total_accessible_rolls += accessible_rolls

		for i in range(len(shelves_index)):
			shelves[shelves_index[i]][square_index[i]] = "X"

print(f"[{total_accessible_rolls}] rolls can be accessed by a forklift.")