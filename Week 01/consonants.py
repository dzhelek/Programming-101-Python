def count_consonants(str):
	r = 0
	consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
	for i in str:
		if i in consonants:
			r += 1
	return r

print(count_consonants('A nice day to code!'))