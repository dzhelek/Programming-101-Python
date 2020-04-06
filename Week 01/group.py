def group(l):
	r = []
	m = l[0]
	c = 0
	for i in l:
		if i == m:
			c += 1
		else:
			r.append([])
			for j in range(c):
				r[-1].append(m)
			c = 1
			m = i
	r.append([])
	for j in range(c):
		r[-1].append(m)
	c = 1
	m = i

	return r


print(group([1,2,1,2,3,3]))
