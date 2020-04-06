import copy


def total_sum(n, m, matrix):
	for i in range(n):
		for j in range(m):
			if matrix[i][j] < 0:
				matrix[i][j] = 0

	return sum([sum(i) for i in matrix])


def matrix_bombing_plan():

	matrix = []
	for i in input("N M: ").split():
		matrix.append(int(i))

	n = matrix[0]
	m = matrix[1]

	matrix = []

	for i in range(m):
		matrix.append([])
		for j in input().split():
			matrix[i].append(int(j))

	result = {}

	for i in range(n):
		for j in range(m):

			new_matrix = copy.deepcopy(matrix)

			if i - 1 >= 0:
				if j - 1 >= 0:
					new_matrix[i-1][j-1] -= matrix[i][j]

				new_matrix[i-1][j] -= matrix[i][j]

				try:
					new_matrix[i-1][j+1] -= matrix[i][j]
				except IndexError:
					pass
				
			if j - 1 >= 0:
				new_matrix[i][j-1] -= matrix[i][j]
			try:
				new_matrix[i][j+1] -= matrix[i][j]
			except IndexError:
				pass


			try:
				if j - 1 >= 0:
					new_matrix[i+1][j-1] -= matrix[i][j]

				new_matrix[i+1][j] -= matrix[i][j]

				try:
					new_matrix[i+1][j+1] -= matrix[i][j]
				except IndexError:
					pass
			except IndexError:
				pass

			result[(i, j)] = total_sum(n, m, new_matrix)

	return result
			

print(matrix_bombing_plan())