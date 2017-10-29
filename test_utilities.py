import unittest

import utilities


class TestCreateGreeting(unittest.TestCase):

    def test_default_greeting(self):
        greeting = utilities.create_greeting()
        self.assertEqual(greeting, 'Hello, World!')

    def test_custom_greeting(self):
        greeting = utilities.create_greeting('Nicole')
        self.assertEqual(greeting, 'Hello, Nicole!')


class TestAppend(unittest.TestCase):

    def test_default_append(self):
        output_list = utilities.append(1)
        output_list = utilities.append(1)
        
        # Appending without providing a list should
        # create a brand new list.
        
        self.assertEqual(output_list, [1])


    def test_custom_append(self):
        input_list = [1, 2, 3]
        output_list = utilities.append(4, input_list)
        self.assertEqual(output_list, [1, 2, 3, 4])

        
class TestAddThreeNumbers(unittest.TestCase):

    def test_add_simple(self):
        output = utilities.add_three_numbers(1, 1, 1)
        self.assertEqual(output, 3)

    def test_add_complex(self):
        output = utilities.add_three_numbers(1, 2, 3)
        self.assertEqual(output, 6)


class TestMultiplyThreeNumbers(unittest.TestCase):

    def test_multiply_simple(self):
        output = utilities.multiply_three_numbers(1, 1, 1)
        self.assertEqual(1, output)

    def test_multiply_complex(self):
        output = utilities.multiply_three_numbers(5, 2, 3)
        self.assertEqual(30, output)

        
if __name__ == '__main__':
    unittest.main()
