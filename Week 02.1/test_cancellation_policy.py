import unittest
from solution_interface import(
    validate_conditions,
    ensure_conditions
)


class TestValidateConditions(unittest.TestCase):
    def test_validation_passes_with_valid_conditions(self):
        conditions = [
            {'hours': 10, 'percent': 10},
            {'percent': 100}
        ]

        validate_conditions(conditions)

    def test_raises_exception_if_all_conditions_have_hours(self):
        conditions = [
            {'hours': 10, 'percent': 10}
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

    def test_raises_exception_if_more_than_one_condition_with_no_hours(self):
        conditions = [
            {'hours': 10, 'percent': 10000},
            {'percent': 10},
            {'percent': 100}
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

    def test_raises_exception_if_hours_bigger_than_24(self):
        # ARRANGE
        conditions = [
            {'hours': 72, 'percent': 10000},
            {'percent': 10},
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Hours cannot be > 24.')


class TestEnsureConditions(unittest.TestCase):
    def test_ensures_all_conditions_have_hours(self):
        conditions = [
            {'hours': 10, 'percent': 10},
            {'percent': 100}
        ]

        ensure_conditions(conditions)

        for condition in conditions:
            self.assertIsNotNone(condition['hours'])


# class TestGroupConditions(unittest.TestCase):
#     def test_


if __name__ == '__main__':
    unittest.main()