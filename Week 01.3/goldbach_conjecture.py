def is_prime(n):
	prime = True
	for i in range(2, n):
		if n % i == 0:
			prime = False
			break
	return prime


def goldbach(n):
	result = []

	for i in range(2, n//2+1):
		if is_prime(i) and is_prime(n-i):
			result.append((i, n-i))

	return result


print(goldbach(100))
