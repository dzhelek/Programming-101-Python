def is_number_balanced(number):
	number = str(number)
	half_n = len(number)//2
	if len(number) % 2:
		number = number[:half_n:] + number[half_n + 1::]
	left = number[:half_n:]
	right = number[half_n::]

	left = [int(i) for i in list(left)]
	right = [int(i) for i in list(right)]

	return sum(left) == sum(right)

print(is_number_balanced(1238033))