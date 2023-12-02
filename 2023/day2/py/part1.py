import regex as re

with open("../input.txt", 'r') as file:
	strings = file.read().splitlines()

MAX_RED		= 12
MAX_GREEN	= 13
MAX_BLUE	= 14

total = 0
for id, string in enumerate(strings):
	id += 1

	cube_list = string.split(":")[1].strip()
	cube_sets = [[x.strip() for x in cube_set.split(", ")] for cube_set in cube_list.split(";")]

	possible = True
	for cube_set in cube_sets:
		red, green, blue = 0, 0, 0
		for cube in cube_set:
			num = int(re.search(r'\d+', cube).group())
			if 'red' in cube:
				red += num
			elif 'green' in cube:
				green += num
			elif 'blue' in cube:
				blue += num
		
		if red > MAX_RED or blue > MAX_BLUE or green > MAX_GREEN:
			possible = False
			break
	
	if possible: total += id

print(total)