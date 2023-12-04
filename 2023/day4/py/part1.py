import regex as re

with open("../input.txt", 'r') as file:
	strings = file.read().splitlines()

total = 0
for string in strings:
	numbers = string.split(":")[1].strip()

	winners, players = [[int(x) for x in re.findall(r'\d+', nums)] for nums in numbers.split("|")]
	wins = sum([1 for winner in winners if winner in players])

	total += 2 ** (wins - 1) if wins else 0

print(total)