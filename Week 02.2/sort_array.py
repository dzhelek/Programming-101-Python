from collect_fraction import simplify_fraction, common_denominator


def sort_fractions(fractions, ascending=True):
	if fractions == []:
		return fractions

	irreducible_fractions = [list(simplify_fraction(fraction)) for fraction in fractions]
	ir_fr = common_denominator(irreducible_fractions)

	if ascending:
		edge = min
	else:
		edge = max

	for i in range(len(ir_fr) - 1):
		edge_i = ir_fr.index(edge(ir_fr[i:]))

		ir_fr[i], ir_fr[edge_i] = ir_fr[edge_i], ir_fr[i]
		fractions[i], fractions[edge_i] = fractions[edge_i], fractions[i]


	return fractions


def main():
	print(sort_fractions([(2,3), (1,2)]))


if __name__ == '__main__':
	main()
