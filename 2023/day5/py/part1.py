import regex as re
from typing import List

# class Mapping:
# 	def __init__(self, map_string):


with open("../input.txt", 'r') as file:
	strings = file.read()#.splitlines()

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


print(seeds)
print(*maps, sep='\n\n')