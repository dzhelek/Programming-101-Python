def increasing_or_decreasing(seq):
	if seq[0] > seq[1]:
		increasing = -1
	elif seq[0] < seq[1]:
		increasing = 1
	else:
		return False

	for i in range(1, len(seq)-1):
		if increasing == 1 and seq[i] > seq[i + 1] or\
			increasing == -1 and seq[i] < seq[i + 1]:
			increasing = 0
			break

	if increasing == 1:
		return "Up!"
	elif increasing == -1:
		return "Down!"
	else:
		return False

print(increasing_or_decreasing([9,8,7,-10]))