def birthday_ranges(birthdays, ranges):
	people = []
	for i in range(len(ranges)):
		people.append(0)
		for j in birthdays:
			if j in range(ranges[i][0], ranges[i][1] + 1):
				people[i] += 1
	return people


print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))