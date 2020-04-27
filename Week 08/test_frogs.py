import unittest

from frogs import (frogs, get_lilies, find_possible_moves, to_tuple)


class TestFrogs(unittest.TestCase):
    def test_even_number_of_lily_pads_raises_error(self):
        n = 8

        with self.assertRaises(AssertionError):
            frogs(n)

    def test_number_of_lily_pads_less_than_three_raises_error(self):
        n = 1

        with self.assertRaises(AssertionError):
            frogs(n)

    def test_get_lilies_on_start(self):
        half_n = 7 // 2

        result = get_lilies(half_n)

        self.assertEqual(result, '>>>_<<<')

    def test_get_finall_lilies(self):
        half_n = 5 // 2

        result = get_lilies(half_n, goal=True)

        self.assertEqual(result, '<<_>>')

    def test_find_possible_moves_with_starting_lake(self):
        lake = get_lilies(3)
        expected = {'>>><_<<', '>>_><<<', '>_>><<<', '>>><<_<'}

        result = find_possible_moves(lake)

        self.assertEqual(result, expected)

    def test_find_possible_moves_with_goal_lake(self):
        lake = get_lilies(3, goal=True)

        result = find_possible_moves(lake)

        self.assertFalse(result, 'possible moves are found when there are not')

    def test_find_possible_moves_with_shuffled_lake(self):
        lake = '<<>_>'
        expected = {'<<_>>'}

        result = find_possible_moves(lake)

        self.assertEqual(result, expected)

    def test_to_tuple_with_no_history(self):
        history = []
        lake = 'd'
        expected = (None, 'd')

        result = to_tuple(history, lake)

        self.assertEqual(result, expected)

    def test_to_tuple_with_last_history_same_as_lake(self):
        lake = 'd'
        history = ['d']
        expected = (None, 'd')

        result = to_tuple(history, lake)

        self.assertEqual(result, expected)

    def test_to_tuple_with_different_history_from_lake(self):
        history = ['b', 'c']
        lake = 'd'
        expected = ('c', 'd')

        result = to_tuple(history, lake)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
