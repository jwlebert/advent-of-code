import regex as re
import time

DIM = 140 - 1

with open("../input.txt", 'r') as file:
	strings = file.read().splitlines()

aaa = []

total = 0
for index, string in enumerate(strings):
	nums = [int(x) for x in re.findall(r'\d+', string)]

	start = 0
	for pos, c in enumerate(string):
		if c.isdigit():
			if start == 0:
				start = pos
			if pos == len(string) - 1:
				print(string[pos], nums[0], pos)
				aaa.append([nums.pop(0), [index, start, pos]])
				start = 0
				continue
			elif not string[pos + 1].isdigit():
				print(string[pos], string[start:pos], nums[0], pos + 1)

				aaa.append([nums.pop(0), [index, start, pos]])
				start = 0
				continue
	
for item in aaa:
	surrounding = ''
	num = item[0]
	row, start, end = item[1]

	bounds = [0, 0, 0, 0]
	if start is not 0: bounds[0] = 1
	if end is not DIM: bounds[1] = 1
	if row is not 0: bounds[2] = 1
	if row is not DIM: bounds[3] = 1

	if bounds[2]: surrounding += strings[row - 1][start - bounds[0]:end + bounds[1] + 1] + '\n'
	surrounding += strings[row][start - bounds[0]:end + bounds[1] + 1] + '\n'
	if bounds[3]: surrounding += strings[row + 1][start - bounds[0]:end + bounds[1] + 1]

	print(surrounding)
	surrounding = surrounding.replace(".", '').strip()
	surrounding = "".join([x for x in surrounding if not x.isdigit()])
	print(surrounding)


	if len(surrounding) > 0:
		print(num)
		total += num

print(total)