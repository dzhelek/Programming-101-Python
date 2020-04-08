import unittest

from compress import compress


class TestCompress(unittest.TestCase):
    def test_with_list_with_one_true_element(self):
        iterable_one = ["Ivo", "Rado", "Panda"]
        iterable_two = [False, False, True]

        result = list(compress(iterable_one, iterable_two))

        self.assertEqual(result, ["Panda"])

    def test_with_range_with_no_true_elements(self):
        iterable_one = range(2)
        iterable_two = [False, False, ]

        result = list(compress(iterable_one, iterable_two))

        self.assertEqual(result, [])

    def test_with_tuple_with_all_true_elements(self):
        iterable_one = ("Ivo", "Rado", "Panda")
        iterable_two = [True, True, True]

        result = list(compress(iterable_one, iterable_two))

        self.assertEqual(result, ["Ivo", "Rado", "Panda"])


if __name__ == '__main__':
    unittest.main()
