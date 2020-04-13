from decimal import Decimal
import unittest

from change_precision import change_precision


class TestChagnePrecision(unittest.TestCase):
    def test_with_correct_with_body(self):
        with change_precision(2):
            result1 = Decimal('1.123132132') + Decimal('2.23232')

        result2 = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(result1, Decimal('3.4'))
        self.assertEqual(result2, Decimal('3.355452132'))

    def test_with_failing_with_body(self):
        with self.assertRaises(Exception):
            with change_precision(2):
                raise Exception

        result = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(result, Decimal('3.355452132'))


if __name__ == '__main__':
    unittest.main()
