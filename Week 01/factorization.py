def prime_factorization(n):
	d = {}
	i = 1
	while n != 1:
		i += 1
		if n % i == 0:
			n /= i
			if i not in d:
				d[i] = 1
			else:
				d[i] += 1
			i -= 1

	return [(x, y) for x, y in d.items()]

print(prime_factorization(1000))
