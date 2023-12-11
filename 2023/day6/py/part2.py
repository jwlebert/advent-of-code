import regex as re


with open("../input.txt", 'r') as file:
	strings = file.read().splitlines()

nums = [re.findall(r"\d+", s) for s in strings]

time, distance = tuple([int(''.join(num)) for num in nums])

total = 0
for dT in range(0, time + 1):
	if dT * (time - dT) > distance:
		total += 1

print(total)