import unittest

from measure_performance import measure_performance


class TestMeasurePerformance(unittest.TestCase):
    def test_(self):
        with measure_performance() as p:
            p.benchmark(restart=True)


if __name__ == '__main__':
    unittest.main()
