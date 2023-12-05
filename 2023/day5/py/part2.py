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

seed_ranges = [
	(seed, seed + seeds[i + 1])
	for i, seed
	in list(enumerate(seeds))[::2]
]

print(seed_ranges)

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

print(maps)


mapped_seeds = []

# this is unrunnable lmao
# so we will write it in rust instead :YAY: ty jerm
for r in seed_ranges:
	for seed in range(*r):
		print(seed)
		s = seed
		for map in maps:
			for (dest, src, length) in map:
				if seed not in range(src, src + length): continue
				seed = dest + seed - src
				break
		mapped_seeds.append(seed)
	
# print(mapped_seeds)
print(min(mapped_seeds))