import regex as re

with open("../input.txt", 'r') as file:
	strings = file.read().splitlines()

total = 0
for string in strings:
	numbers = string.split(":")[1].strip()
	# for nums in numbers.split("|"):
	# 	for x in nums.strip().split(" "):
	# 		print(int(x.strip()))
	winners, players = [[int(x) for x in re.findall(r'\d+', nums)] for nums in numbers.split("|")]

	card_val = 0
	for winning_num in winners:
		if winning_num in players:
			if card_val == 0: card_val = 1
			else: card_val *= 2

	total += card_val

print(total)