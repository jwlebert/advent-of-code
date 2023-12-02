import regex as re

with open("../input.txt", 'r') as file:
	strings = file.read().splitlines()

total = 0
for id, string in enumerate(strings):
	id += 1

	cube_list = string.split(":")[1].strip()
	cube_sets = [[x.strip() for x in cube_set.split(", ")] for cube_set in cube_list.split(";")]
	
	red, green, blue = 0, 0, 0
	for cSet in cube_sets:
		for cube in cSet:
			num = int(re.search(r'\d+', cube).group())
			if 'red' in cube:
				if num > red: red = num
			elif 'green' in cube:
				if num > green: green = num
			elif 'blue' in cube:
				if num > blue: blue = num
	
	total += red * green * blue

print(total)