from cat import sys, cat


def main():
    for i in range(1, len(sys.argv)):
    	cat(sys.argv[i])
    	print()
   

if __name__ == '__main__':
    main()