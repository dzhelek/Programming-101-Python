def to_digits(n):
	return list(map(int, list(str(n))))
	# return [int(i) for i in str(digits)]

print(to_digits(123023))