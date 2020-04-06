def max_consecutive(items):
	r = []
	m = items[0]
	c = 0
	for i in items:
		if i == m:
			c += 1
		else:
			r.append(c)
			c = 1
			m = i
	r.append(c)

	return max(r)

print(max_consecutive([1,1,2,2,3,3,4,4,5,5,5]))
