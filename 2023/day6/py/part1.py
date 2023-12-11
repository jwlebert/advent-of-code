import regex as re


with open("../input.txt", 'r') as file:
	strings = file.read().splitlines()

nums = [[int(n) for n in re.findall(r"\d+", s)] for s in strings]

pairs = [(t, nums[1][i]) for i, t in enumerate(nums[0])]

total = 1
for time, distance in pairs:
	winning_matches = 0
	for dT in range(0, time + 1):
		if dT * (time - dT) > distance:
			winning_matches += 1
	total *= winning_matches

print(total)