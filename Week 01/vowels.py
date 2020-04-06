def count_vowels(str):
	r = 0
	vowels = "AEIOUYaeiouy"
	for i in str:
		if i in vowels:
			r += 1
	return r

print(count_vowels('A nice day to code!'))