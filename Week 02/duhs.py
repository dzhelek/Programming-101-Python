import os
import sys


def du_hs(path):
	size = 0
	for dirpath, dirnames, filenames in os.walk(path):
		print('filename ', filenames)
		for file in filenames:
			file_path = os.path.join(dirpath, file)
			# size += os.statvfs(path).f_bsize

			size += os.path.getsize(file_path)
	return str(size/1024) + 'K'

def main():
	print(du_hs(sys.argv[1]))


if __name__ == '__main__':
	main()