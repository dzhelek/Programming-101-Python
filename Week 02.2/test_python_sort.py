import unittest
from python_sort import(
    my_sort,
    sort_list,
    validate_iterable
)


class TestSortList(unittest.TestCase):
    def test_with_given_empty_list_should_return_empty_list(self):
        lst = []

        result = sort_list(lst, True, 0)

        self.assertEqual(result, [])


    def test_with_given_list_of_exactly_one_element_should_return_itself(self):
        lst = [9]
        expected = [9]

        result = sort_list(lst, True, 0)

        self.assertEqual(result, expected)  


    def test_with_False_ascending_should_return_it_descending(self):
        lst = [10, 8, 9, 10, 100]
        expected = [100,10,10,9,8]

        result = sort_list(lst, False, 0)

        self.assertEqual(result, expected)  


class TestMySort(unittest.TestCase):
    def test_with_given_touple_should_return_sorted_tuple(self):
        to_sort = (10,8,9,10,100)
        expected = (8,9,10,10,100)

        result = my_sort(to_sort)

        self.assertEqual(result, expected)


    def test_with_given_nothing_should_return_empty_list(self):

        result = my_sort()

        self.assertEqual(result, [])


    def test_with_given_list_of_dicts_should_sort_them(self):
        to_sort = [{'h': 10}, {'h': 5}]
        expected = [{'h': 5}, {'h': 10}]

        result = my_sort(to_sort, key='h')

        self.assertEqual(result, expected)


class TestValidateIterable(unittest.TestCase):
    def test_with_list_of_not_integers_raises_error(self):
        to_sort = ['ll', 'l']
        exc = None

        try:
            validate_iterable(to_sort, 0)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Cannot sort iterable with not-integer element!')


    def test_with_heterogeneous_iterable_raises_error(self):
        to_sort = [90, {'h': 5}]
        exc = None

        try:
            validate_iterable(to_sort, 0)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Cannot sort heterogeneous iterable!')


    def test_with_dictionary_with_element_with_wrong_key_raises_error(self):
        to_sort = [{'h': 90}, {'k':90}]
        exc = None

        try:
            validate_iterable(to_sort, key='h')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), "There is element with no 'h' key!")


    def test_with_given_not_iterable_raises_error(self):
        exc = None

        try:
            validate_iterable(8, 5)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), "Could sort only tuples and lists!")


if __name__ == '__main__':
    unittest.main()