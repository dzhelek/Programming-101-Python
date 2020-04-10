import unittest

from book_generator import (generate_filenames,
                            generate_words)


class TestBookGenerator(unittest.TestCase):
    def test_generate_filenames_on_fist_call(self):
        file = generate_filenames()

        result = next(file)

        self.assertEqual(result, '001.txt')

    def test_generate_filenames_on_999th_call(self):
        file = generate_filenames()
        for i in range(999):
            result = next(file)

        self.assertEqual(result, '999.txt')

    def test_generate_words_should_every_word_end_with_space(self):
        word = generate_words()

        result1 = next(word)
        result2 = next(word)

        self.assertTrue(result1.endswith(' '))
        self.assertTrue(result2.endswith(' '))


if __name__ == '__main__':
    unittest.main()