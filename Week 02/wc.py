import sys


def chars(file):
	with open(file, 'r') as f:
		return len(f.read())


def words(file):
	with open(file, 'r') as f:
		return len(f.read().split())


def lines(file):
	with open(file, 'r') as f:
		return len(f.readlines())


def main():
	if sys.argv[1] == 'chars':
		print(chars(sys.argv[2]))
	elif sys.argv[1] == 'words':
		print(words(sys.argv[2]))
	elif sys.argv[1] == 'lines':
		print(lines(sys.argv[2]))
	else:
		raise ValueError("wc.py's first argument should be one of: ('chars', 'words', 'lines')!")

if __name__ == '__main__':
	main()