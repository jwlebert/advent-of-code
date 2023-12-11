import regex as re


with open("../input.txt", 'r') as file:
	strings = file.read().splitlines()

nums = [[int(n) for n in re.findall(r"-?\d+", s)] for s in strings]
# the `-?` in the regex includes the negatives in negative numbers

total = 0
for history in nums:
	index = 0
	diffs = [history]
	while len([x for x in diffs[index] if x != 0]):
		cur_list = diffs[index]
		new_list = []
		for i in range(1, len(cur_list)):
			new_list.append(cur_list[i] - cur_list[i - 1])
		diffs.append(new_list)
		index += 1

	next_val = 0
	for diff in diffs:
		next_val += diff[-1]
	total += next_val

print(total)