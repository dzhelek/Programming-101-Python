def palindrome(n):
	n = list(str(n))
	for i in range(len(n)//2):
		if n[0] == n[-1]:
			n.pop(0)
			try:
				n.pop(-1)
			except IndexError:
				pass
	if n:
		return False
	else:
		return True

print(palindrome("baba"))