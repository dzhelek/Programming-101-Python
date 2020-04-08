import unittest
from silence import silence


class TestSilence(unittest.TestCase):
    def test_with_an_error_should_pass(self):
        @silence('errors.txt')
        def foo(x):
            if x > 50:
                raise ValueError('Omg.')
        try:
            foo(100)
        except Exception as err:
            self.fail(err)

    def test_with_arguments_number_error_should_pass(self):
        @silence('errors.txt')
        def foo(x, y):
            pass
        try:
            foo(100, 200, 300)
        except Exception as err:
            self.fail(err)

    def test_with_no_error_should_pass(self):
        @silence('errors.txt')
        def foo(x):
            if x > 50:
                raise ValueError('Omg.')
        try:
            foo(50)
        except Exception as err:
            self.fail(err)


if __name__ == '__main__':
    unittest.main()
