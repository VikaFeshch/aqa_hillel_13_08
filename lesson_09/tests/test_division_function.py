import unittest

from lesson_09.src.functions import division

# test suite
# class - CamelCase
class TestDivisionFunction(unittest.TestCase):

    # test case, snake_case
    def test_division_positive(self):
        result = division(1, 2)
        self.assertEqual(result, 0.5, msg=f"Result {result} is not as expected 0.5")

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(1, 0)

    def test_divide_by_zero_no_with(self):
        try:
            result = division(1, 0)
        except ZeroDivisionError:
            pass
        else:
            self.fail("ZeroDivisionError is not raised")

if __name__ == '__main__':
    unittest.main() # test runer