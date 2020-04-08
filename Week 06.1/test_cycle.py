import unittest

from cycle import cycle


class TestCycle(unittest.TestCase):
    def test_no_raises(self):
        endless = cycle(range(0, 10))

        try:
            for _ in range(50):
                next(endless)
        except Exception as exc:
            self.fail(exc)


if __name__ == '__main__':
    unittest.main()
