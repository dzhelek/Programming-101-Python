import unittest

from silence_errors import silence_exception


class TestSilenceException(unittest.TestCase):
    def test_with_same_error_should_not_raise(self):
        with silence_exception(ValueError):
            # nothing should happen
            raise ValueError('Test')

    def test_with_different_errors_should_reraise(self):
        with self.assertRaises(TypeError):
            with silence_exception(ValueError):
                # the error should be re-raised since it is not expected.
                raise TypeError('Test')

    def test_with_same_error_and_message_should_not_raise(self):
        with silence_exception(ValueError, 'Test'):
            # nothing should happen
            raise ValueError('Test')

    def test_with_same_error_but_different_message_should_raise(self):
        with self.assertRaises(ValueError):
            with silence_exception(ValueError, 'Testing.'):
                # the error should be re-raised since it is not expected.
                raise ValueError('Test')

    def test_with_differents_error_but_same_message_should_raise(self):
        with self.assertRaises(TypeError):
            with silence_exception(ValueError, 'Test'):
                raise TypeError('Test')


if __name__ == '__main__':
    unittest.main()
