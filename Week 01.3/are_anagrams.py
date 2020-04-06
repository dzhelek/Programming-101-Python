def are_anagrams(word1, word2):
	set1 = set(word1)
	set2 = set(word2)
	return not (set1 - set2 or set2 - set1) and len(word1) == len(word2)


arr = []
for x in input().split():
	arr.append(x)
if are_anagrams(arr[0].lower(), arr[1].lower()):
	print('ANAGRAMS')
else:
	print('NOT ANAGRAMS')