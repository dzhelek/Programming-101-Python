def get_largest_palindrome(n):
	str_n = str(n)
	half_len = len(str_n)//2

	half_n = str_n[:half_len]	

	if len(str(n)) % 2:
		palindrome_n = half_n + str_n[half_len] + half_n[::-1]

		if int(palindrome_n) >= n:
			new_half_n = str(int(half_n + str_n[half_len]) - 1)
			return new_half_n + half_n[::-1]
	else:
		palindrome_n = half_n + half_n[::-1]

		if int(palindrome_n) >= n:
			half_n = str(int(half_n) - 1)
			return half_n + half_n[::-1]
		else:
			return palindrome_n


print(get_largest_palindrome(1000))
