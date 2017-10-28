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

