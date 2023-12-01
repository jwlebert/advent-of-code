import regex as re
from typing import List


def find_numbers(input: List[str], include_strs: bool = False):
	if include_strs:
		# thanks jerm for "inspiration" for regex
		num_list = [re.findall(r"(\d|zero|one|two|three|four|five|six|seven|eight|nine)", line, overlapped=True) for line in input]
		# the first arg accepts all digits (\d) and all word versions of digits
		# the second arg is what will be regexed
		# overlapped means the things can overlap, ie, "eightwo" -> 8, 2 and not 8

		word_to_num = {
			'zero': 0,
			'one': 1,
			'two': 2,
			'three': 3,
			'four': 4,
			'five': 5,
			'six': 6,
			'seven': 7,
			'eight': 8,
			'nine': 9
		}

		ints = [
			[int(n) if n.isdigit() else word_to_num[n] for n in nums]
			for nums in num_list
		]
		
		value = sum([int(i[0] * 10 + i[-1]) for i in ints])
	else:
		num_list = [[c for c in line if c.isdigit()] for line in input]
		value = sum([int(num[0] + num[-1]) for num in num_list])
	return value

with open("../input.txt", 'r') as f:
	strings = f.read().splitlines()


print(f"Part One : {find_numbers(strings)}")
print(f"Part Two : {find_numbers(strings, include_strs=True)}")