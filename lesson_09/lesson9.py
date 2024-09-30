import unittest

from lesson_09.src.functions import division


class TestDivideFunction(unittest.TestCase):
	def test_divide_by_zero(self):
	    result = division(10, 0)
        with self.assertRaises(ZeroDivisionErrorr, result)

if __name__ == '__main__':
    unittest.main()