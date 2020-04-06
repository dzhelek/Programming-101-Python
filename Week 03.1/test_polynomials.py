import unittest
from polynomials import Term, check


class TestPolynomial(unittest.TestCase):
    def test_check_with_correct_input(self):
        p = "1+x^2"
        
        result = check(p)

        self.assertTrue(result, "polynomial is not checked correctly")


    def test_check_with_more_than_one_no_x_monominals(self):
        p = "x^3+2+5"
        exc = None

        try:
            result = check(p)
        except AssertionError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), "invalid input!")


    def test_check_with_other_integer(self):
        p = "y^3+y^2"
        
        result = check(p)

        self.assertTrue(result, "polynomial is not checked correctly")


if __name__ == '__main__':
    unittest.main()
