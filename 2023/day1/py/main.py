from typing import List


def find_numbers(input: List[str], include_strs: bool = False):
	if not include_strs:
		all_nums = [[c for c in line if c.isdigit()] for line in input]
		value = sum([int(num[0] + num[-1]) for num in all_nums])
	return value

with open("../input.txt", 'r') as f:
	strings = f.read().splitlines()


print(f"Part One : {find_numbers(strings)}")

