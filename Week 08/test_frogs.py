import unittest

from frogs import (frogs, get_lilies, find_possible_moves)


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

    def test_with_one_pair_frogs(self):
        frogs(5)


if __name__ == '__main__':
    unittest.main()
