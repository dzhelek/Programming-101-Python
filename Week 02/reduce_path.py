def reduce_file_path(file_path):
	while '//' in file_path:
		file_path = file_path.replace('//', '/')

	while '/..' in file_path:
		file_path = file_path.partition('/..')
		left = file_path[0]
		left = left.rpartition('/')[0]

		file_path = left + file_path[2]

	while '/.' in file_path:
		file_path = "".join(file_path.split('/.'))

	file_path = file_path.rstrip('/')

	if file_path:
		return file_path
	else:
		return '/'



def main():
	print(reduce_file_path("/home//rositsazz/courses/./Programming101-Python/week01/../"))


if __name__ == '__main__':
	main()