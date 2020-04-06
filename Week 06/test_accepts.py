import unittest
from accepts import accepts


class TestAccepts(unittest.TestCase):
    def test_with_str_incorrect_raises_error(self):
        @accepts(str)
        def say_hello(name):
            return "Hello, I am {}".format(name)

        with self.assertRaises(TypeError):
            say_hello(4)

    def test_with_two_correct_arguments_does_not_raise_error(self):
        @accepts(str, int)
        def deposit(name, money):
            print("{} sends {} $!".format(name, money))

        deposit("Marto", 10)

    def test_with_one_correct_argument_and_one_incorrect_raises_error(self):
        @accepts(str, int)
        def deposit(name, money):
            print("{} sends {} $!".format(name, money))

        with self.assertRaises(TypeError):
            deposit("Marto", "Marto")


if __name__ == '__main__':
    unittest.main()
