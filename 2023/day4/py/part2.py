import regex as re

with open("../input.txt", 'r') as file:
	strings = file.read().splitlines()

total = 0

cards = []

for string in strings:
	numbers = string.split(":")[1].strip()
	card = [[int(x) for x in re.findall(r'\d+', nums)] for nums in numbers.split("|")]

	cards.append([
		card, 1
	])

for id, ((winners, players), _) in enumerate(cards):
	wins = sum([1 for winner in winners if winner in players])
	
	for index in range(id + 1, id + 1 + wins):
		cards[index][1] += cards[id][1]

for _, amount in cards:
	total += amount

print(total)