def nan_expand(times):
	r = ""
	for x in range(times):
		r += "Not a "
	if r:
		r += "NaN"

	return r

print(nan_expand(3))
