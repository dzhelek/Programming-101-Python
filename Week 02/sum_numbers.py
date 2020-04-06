import sys

def sum_numbers(filename):
	with open(filename, 'r') as f:
		return sum([int(i) for i in f.read().split()])

def main():
	print(sum_numbers(sys.argv[1]))

if __name__ == '__main__':
	main()