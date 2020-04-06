def factorial(n):
	if n < 2:
		return 1
	else:
		return n*factorial(n-1)

def fact_digits(n):
	r = 0
	for i in list(str(n)):
		r += factorial(int(i))

	return r

print(fact_digits(999))