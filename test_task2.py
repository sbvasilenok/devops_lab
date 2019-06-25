#!/usr/bin/env python

import unittest
from pd import palyndrome_detect


class TestPal(unittest.TestCase):
    def test_correct_palyndrome_detect(self):
        """
        Correct palindrome test 1
        """
        data = 'qwertyytrewq'
        self.assertTrue(palyndrome_detect(data))

        """
        Correct palindrome test 2
        """
        data = 'qw e rtyy t r ew q'
        self.assertTrue(palyndrome_detect(data))

    def test_incorrect_palyndrome_detect(self):
        """
        Inorrect palindrome test 1
        """
        data = 'qwertyqwerty'
        self.assertFalse(palyndrome_detect(data))

        """
        Inorrect palindrome test 2
        """
        data = 'qwertyutrewq'
        self.assertFalse(palyndrome_detect(data))

        """
        Inorrect palindrome test 3
        """
        data = 'qwer xt rewq'
        self.assertFalse(palyndrome_detect(data))


if __name__ == '__main__':
    unittest.main()
