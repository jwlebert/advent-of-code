import regex as re


with open("../ex_input.txt", 'r') as file:
	strings = file.read()

seeds = [
	int(seed)
	for seed
	in [
		map_str.split('\n') for map_str in strings.split(":")
	][1][:-2][0].split()
]

maps = [
	[
		[
			int(n)
			for n
			in re.findall(r'\d+', a)
		]
		for a
		in mapping
		if len(re.findall(r'\d+', a)) > 0
	]
	for mapping
	in [
		map_str.split('\n') for map_str in strings.split(":")
	]
][2:]

mapped_seeds = []

for seed in seeds:
	for map in maps:
		for (dest, src, length) in map:
			if seed not in range(src, src + length + 1): continue
			distance = seed - src
			seed = dest + distance
			break
	mapped_seeds.append(seed)
	
print(min(mapped_seeds))