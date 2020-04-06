import unittest
from sort_array import sort_fractions


class TestSortFractions(unittest.TestCase):
	def test_with_two_fractions(self):
		fractions = [(2, 3), (1, 2)]
		excpected = [(1, 2), (2, 3)]

		fractions = sort_fractions(fractions)

		self.assertEqual(fractions, excpected)


	def test_with_descending_argument_given(self):
		fractions = [(2, 3), (1, 2), (1, 3)]
		excpected = [(2, 3), (1, 2), (1, 3)]

		fractions = sort_fractions(fractions, ascending=False)

		self.assertEqual(fractions, excpected)


	def test_with_only_one_fraction_shall_return_it(self):
		fractions = [(2, 50)]

		result = sort_fractions(fractions, ascending=False)

		self.assertEqual(result, fractions)


	def test_with_no_fractions(self):
		fractions = []

		result = sort_fractions(fractions, ascending=False)

		self.assertEqual(result, fractions)


	def test_with_negative_element(self):
		fractions = [(5, 6), (22, 78), (22, 7), (7, 8), (-9, 6), (15, 32)]
		excpected = [(-9, 6), (22, 78), (15, 32), (5, 6), (7, 8), (22, 7)]

		fractions = sort_fractions(fractions)

		self.assertEqual(fractions, excpected)


if __name__ == '__main__':
	unittest.main()