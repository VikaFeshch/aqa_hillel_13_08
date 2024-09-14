import unittest

from lesson_09.src.homework_09 import average_of_list, find_substring, change_formate_date, count_words


#from lesson_09.src.homework_09 import average_of_list

class TestAverageOfList(unittest.TestCase):

    def test_aver_positive_nums(self):
        list_for_count = (1, 2, 3, 4, 5, 6, 7, 8, 9, 12)
        expected_result = 5.7
        result = average_of_list(list_for_count)
        self.assertEqual(result, expected_result, msg=f"Actual result {result} is not as expected {expected_result}")


    def test_aver_negative_nums(self):
        list_for_count = (-1, -2, -3, -4, -5, -6, -7, -8, -9, -12)
        expected_result = -5.7
        result = average_of_list(list_for_count)
        self.assertEqual(result, expected_result, msg=f"Actual result {result} is not as expected {expected_result}")

    def test_aver_include_Zero(self):
        list_for_count = (0, 0 ,0, 0, 0, 0)
        expected_result = 0
        result = average_of_list(list_for_count)
        self.assertEqual(result, expected_result, msg=f"Actual result {result} is not as expected {expected_result}")

    def test_aver_over_nums(self):
        list_for_count = (-10000000000000000, -2000000000000000, -3, -4, 55698914269841825, 0, 7, 8, 9, 12)
        expected_result = 4369891426984185.5
        result = average_of_list(list_for_count)
        self.assertEqual(result, expected_result, msg=f"Actual result {result} is not as expected {expected_result}")


    def test_aver_mix_nums(self):
        list_for_count = (-1, -2, -3, -4, -5, 6, 7, 8, 9, 12)
        expected_result = 2.7
        result = average_of_list(list_for_count)
        self.assertEqual(result, expected_result, msg=f"Actual result {result} is not as expected {expected_result}")


    def test_aver_empty_list(self):
        list_for_count = ()
        expected_error = ZeroDivisionError
        with self.assertRaises(expected_error):
            average_of_list(list_for_count)



    def test_aver_not_valid_list(self):
        list_for_count = (-1, -2, -3, -4, -5, 6, 7, 8, "%", "12")
        expected_error = TypeError
        expected_message = "unsupported operand type(s) for +: 'int' and 'str'"
        with self.assertRaises(expected_error) as cm:
            average_of_list(list_for_count)
        the_exception = cm.exception
        actual_message = the_exception.args[0]
        self.assertEqual(actual_message, expected_message)

class TestFindSubstring(unittest.TestCase):

    def test_find_substring_positive(self):
        str1 = "Hello, world!"
        str2 = "world"
        expected_result = 7
        result = find_substring(str1, str2)
        self.assertEqual(result, expected_result, msg=f"Actual result {result} is not as expected {expected_result}")

    def test_find_substring_negative(self):
        str1 = "Hello, world!"
        str2 = "Good buy"
        expected_result = -1
        result = find_substring(str1, str2)
        self.assertEqual(result, expected_result, msg=f"Actual result {result} is not as expected {expected_result}")

class TestChangeFormateDate(unittest.TestCase):

    def test_change_formate_date(self):
        inp_date = 11, 22, 2003
        expected_result = '11.22.2003'
        result = change_formate_date(inp_date)
        self.assertEqual(result, expected_result, msg=f"Actual result {result} is not as expected {expected_result}")

class TestCountWords(unittest.TestCase):

    def test_count_words(self):
        inp_date = """London is the capital and largest city of both England and the United Kingdom, with a population
of 8,866,180 in 2022. The wider metropolitan area is the largest in Western Europe, with a population of 14.9 million. 
London stands on the River Thames in southeast England, at the head of a 50-mile (80 km) estuary down to the North Sea, 
and has been a major settlement for nearly 2,000 years."""
        expected_result = 33
        result = count_words(inp_date)
        self.assertEqual(result, expected_result, msg=f"Actual result {result} is not as expected {expected_result}")


if __name__ == '__main__':
    unittest.main()
