def sum_of_digits(n):
	n = str(n)
	if n[0] == '-':
		n = n[1::]
	#m = 0
	#for i in range(len(n)):
	#	m += int(n[i])

	return sum([int(i) for i in n])

	return m

print(sum_of_digits(-10))