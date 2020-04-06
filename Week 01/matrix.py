def sum_matrix(m):
	r = 0
	for i in m:
		for j in i:
			r += j

	return r

print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))