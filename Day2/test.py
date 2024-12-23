import unittest

from day2 import IsValid

class testDay2(unittest.TestCase):
    def test_all_descending_is_safe(self):
        b = [7, 6, 4, 2, 1]

        self.assertTrue(IsValid(b))

    def test_increase_of_5_is_unsafe(self):
        set = [1, 2, 7, 8, 9]
        
        self.assertFalse(IsValid(set))

    def test_decrease_of_4_is_unsafe(self):
        set = [9, 7, 6, 2, 1]

        self.assertFalse(IsValid(set))
    
    def test_decrease_mixid_with_increase_is_unsafe(self):
        set = [1, 3, 2, 4, 5]

        self.assertFalse(IsValid(set))
    
    def test_same_number_is_unsafe(self):
        set = [8, 6, 4, 4, 1]
        self.assertFalse(IsValid(set))

    def test_increasing_is_safe(self):
        set = [1, 3, 6, 7, 9]
        self.assertTrue(IsValid(set))

if __name__ == '__main__':
    unittest.main()