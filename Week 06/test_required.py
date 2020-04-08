import unittest

from required import required


class TestRequired(unittest.TestCase):
    def test_with_one_required_function(self):
        class Animal:
            @required
            def eat(self, food):
                pass

        class Panda(Animal):
            pass

        with self.assertRaises(Exception):
            p = Panda()

# Exception: All classes that inherit from "Animal" must provide "eat" method.


if __name__ == '__main__':
    unittest.main()