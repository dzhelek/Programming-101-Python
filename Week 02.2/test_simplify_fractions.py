import unittest
from simplify_fractions import(
    simplify_positive_fraction,
    simplify_fraction
)


class TestSimplifyPositiveFraction(unittest.TestCase):
    def test_with_irreducible_fraction_shall_return_it(self):
        fraction = (100, 13)

        result = simplify_positive_fraction(fraction)

        self.assertEqual(fraction, result)


    def test_with_reducible_fraction_shall_reduce_it(self):
        fraction = (3, 9)

        result = simplify_positive_fraction(fraction)

        self.assertEqual(result, (1, 3))


    def test_with_nominator_zero_shall_return_zero_over_one(self):
        fraction = (0, 100)

        result = simplify_positive_fraction(fraction)

        self.assertEqual(result, (0,1))


    def test_with_denominator_one_shall_return_it(self):
        fraction = (100, 1)

        result = simplify_positive_fraction(fraction)

        self.assertEqual(fraction, result)


    def test_with_nominator_one_shall_return_it(self):
        fraction = (1, 100)

        result = simplify_positive_fraction(fraction)

        self.assertEqual(fraction, result)


class TestSimplifyFractions(unittest.TestCase):
    def test_with_negative_nominator_and_denominator_shall_reduce_it_like_positive(self):
        fraction = (-2, -10)

        result = simplify_fraction(fraction)

        self.assertEqual(result, (1, 5))


    def test_with_denominator_zero_shall_raise_error(self):
        fraction = (1, 0)
        exc = None

        try:        
            simplify_fraction(fraction)
        except Exception as e:
            exc = e

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), "Denominator cannot be equal to zero!")


    def test_with_only_nominator_or_dominator_negative_shall_return_negative_nominator(self):
        fraction = (-2, 10)

        result = simplify_fraction(fraction)

        self.assertEqual(result, (-1, 5))


    def test_with_float(self):
        fraction = (3.5, 0.5)

        result = simplify_fraction(fraction)

        self.assertEqual(result, (7, 1))


if __name__ == '__main__':
    unittest.main()
