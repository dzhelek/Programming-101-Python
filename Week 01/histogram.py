def char_histogram(string):
	r = {}
	for i in string:
		if i in r:
			r[i] += 1
		else:
			r[i] = 1
	return r

print(char_histogram("AAAAaaa!!!"))