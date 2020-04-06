def sum_of_numbers(input_string):
	result = []
	j = 0
	sequence_of_letters = 0
	sequence_of_digits = 0
	for i in input_string:
		try:
			int(i)
		except ValueError:
			sequence_of_digits = 0
			if not sequence_of_letters:
				j += 1
				sequence_of_letters = 1
		else:
			if not sequence_of_digits:
				result.append(int(i))
				sequence_of_digits = 1
			else:
				try:
					result[j] *= 10
				except IndexError:
					j -= 1
					result[j] *= 10
				finally:
					result[j] += int(i)

			sequence_of_letters = 0

	return sum(result)


print(sum_of_numbers("1111O"))