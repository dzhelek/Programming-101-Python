import unittest

from chain import chain


class TestChain(unittest.TestCase):
    def test_with_ranges(self):
        list1 = range(0, 4)
        list2 = range(4, 8)

        result = list(chain(list1, list2))

        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7])

    def test_with_lists(self):
        list1 = [0, 1, 2, 3]
        list2 = [4, 5, 6, 7]

        result = list(chain(list1, list2))

        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7])

    def test_with_tuples(self):
        list1 = (0, 1, 2, 3)
        list2 = (4, 5, 6, 7)

        result = list(chain(list1, list2))

        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7])

    def test_with_sets(self):
        list1 = {0, 1, 2, 3}
        list2 = {4, 5, 6, 7}

        result = list(chain(list1, list2))

        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7])

    def test_wiht_dicts(self):
        list1 = {0: 0, 1: 0, 2: 0, 3: 0}
        list2 = {4: 1, 5: 0, 6: 0, 7: 0}

        result = list(chain(list1, list2))

        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7])

    def test_with_strings(self):
        list1 = '0123'
        list2 = '4567'

        result = list(chain(list1, list2))

        self.assertEqual(result, ['0', '1', '2', '3', '4', '5', '6', '7'])

    def test_with_file_objects(self):
        with open('iterable1.txt', 'w') as f:
            f.write('0123')
        with open('iterable2.txt', 'w') as f:
            f.write('4567')
        with open('iterable1.txt', 'r') as f:
            list1 = f.read()
        with open('iterable2.txt', 'r') as f:
            list2 = f.read()

        result = list(chain(list1, list2))

        self.assertEqual(result, ['0', '1', '2', '3', '4', '5', '6', '7'])


if __name__ == '__main__':
    unittest.main()
