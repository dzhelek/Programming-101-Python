import unittest
from collect_fraction import(
	common_denominator,
	collect_fractions,
)


class TestCollectFractions(unittest.TestCase):
	def test_with_not_self_prime_denominators(self):
		fractions = [(1, 4), (1, 2)]
		expected = (3,4)

		fractions = collect_fractions(fractions)

		self.assertEqual(fractions, expected)


	def test_with_only_one_fraction_shall_return_it(self):
		fractions = [(2, 10)]

		fractions = collect_fractions(fractions)

		self.assertEqual(fractions, (1, 5))


	def test_with_negative_fractions(self):
		fractions = [(1, 7), (-1, 2)]

		fractions = collect_fractions(fractions)

		self.assertEqual(fractions, (-5, 14))


class TestCommonDenominator(unittest.TestCase):
	def test_with_not_self_prime_denominators(self):
		fractions = [[1, 4], [1, 2]]
		expected = [[1,4], [2,4]]

		fractions = common_denominator(fractions)

		self.assertEqual(fractions, expected)


	def test_with_self_prime_denominators(self):
		fractions = [[1, 7], [2, 6]]
		expected = [[6,42], [14,42]]

		result = common_denominator(fractions)

		self.assertEqual(result, expected)



if __name__ == '__main__':
	unittest.main()
