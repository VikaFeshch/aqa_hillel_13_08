import unittest


from lesson_09.src.functions import add

# test suite
# class - CamelCase
class TestAddFunction(unittest.TestCase):

    # test case, snake_case
    def test_add_positive(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    # test case
    def test_add_negative(self):
        result = add(-100, -200)
        self.assertEqual(result, -300)

    def test_dict(self):
        pass


if __name__ == '__main__':
    unittest.main() # test runer
