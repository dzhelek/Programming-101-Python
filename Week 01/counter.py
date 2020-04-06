def is_palindrome(word):
	return word == word[::-1]

def contains_word(word, text):
	if is_palindrome(word):
		return text.count(word)

	return text.count(word) + text[::-1].count(word)

def main():
	word = input()
	arr = []
	for i in input().split():
		arr.append(int(i))
	y = arr[0]
	x = arr[1]

	if len(word) > x and len(word) > y:
		return "Invalid number of rows or columns!"

	arr = []
	for i in range(y):
		arr.append([])
		for j in input().split():
			arr[i].append(j)


	c = 0

	for row in arr:
		c += contains_word(word, "".join(row))

	for i in range(x):
		column = []
		for row in arr:
			column.append(row[i])

		c += contains_word(word, "".join(column))

	for k in range(x + y -1):
		diagonal = []
		for i in range(y):
			for j in range(x):
				if i + j == k:
					diagonal.append(arr[i][j])
		c += contains_word(word, "".join(diagonal))

	for k in range(1-x, y):
		diagonal = []
		for i in range(y):
			for j in reversed(range(x)):
				if j - i == k:
					diagonal.append(arr[i][j])
		c += contains_word(word, "".join(diagonal))

	# for i in arr:
	# 	for j in range(x):
	# 		if i[j] == word[k]:
	# 			if k == len(word)-1:
	# 				c += 1
	# 				k = 0
	# 			else:
	# 				k += 1

	# k = 0

	# for i in arr:
	# 	for j in i:
	# 		if i[j] == word[k]:
	# 			if k != len(word)-1:
	# 				k += 1
	# 				if i[j+1]


	return c

print(main())