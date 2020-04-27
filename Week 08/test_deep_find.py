import unittest

from deep_find import deep_find_dfs


class TestDeepFindDFS(unittest.TestCase):
    # def test_with_plain_dictionary(self):
    #     d = {'e1': 5, 'e2': 's'}

    #     result1 = deep_find_dfs(d, 'e1')
    #     result2 = deep_find_dfs(d, 'e2')

    #     self.assertEqual(result1, 5)
    #     self.assertEqual(result2, 's')

    def test_with_dictionary_of_dictionaries(self):
        d = {
            'd1': {'e1': 5, 'e2': 's'},
            'd2': {'e3': 8, 'e4': 't'},
        }

        # result1 = deep_find_dfs(d, 'e1')
        result2 = deep_find_dfs(d, 'e4')

        # self.assertEqual(result1, 5)
        self.assertEqual(result2, 't')


if __name__ == '__main__':
    unittest.main()
