import unittest
from sort import *

class TestSort(unittest.TestCase):
    ### isHeavy tests ###
    def test_isHeavy_negativeThrows(self):
        with self.assertRaises(Exception):
            isHeavy(-1)
            
    def test_isHeavy_zeroThrows(self):
        with self.assertRaises(Exception):
            isHeavy(0)
            
    def test_isHeavy_lessThan20IsFalse(self):
        self.assertFalse(isHeavy(5))
            
    def test_isHeavy_greaterThan20IsTrue(self):
        self.assertTrue(isHeavy(21))

    
    ### isBulky tests ###
    def test_isBulky_negativeThrows(self):
        with self.assertRaises(Exception):
            isBulky(-1, 5, 5)
        with self.assertRaises(Exception):
            isBulky(5, -1, 5)
        with self.assertRaises(Exception):
            isBulky(5, 5, -1)
            
    def test_isBulky_zeroThrows(self):
        with self.assertRaises(Exception):
            isBulky(0, 5, 5)
        with self.assertRaises(Exception):
            isBulky(5, 0, 5)
        with self.assertRaises(Exception):
            isBulky(5, 5, 0)
            
    def test_isBulky_greaterThan150ReturnsTrue(self):
        self.assertTrue(isBulky(150, 5, 5))
        self.assertTrue(isBulky(5, 151, 5))
        self.assertTrue(isBulky(5, 5, 152))
            
    def test_isBulky_volumnLessThan1MillionReturnsFalse(self):
        self.assertFalse(isBulky(5, 5, 5))
            
    def test_isBulky_volumnGreaterThan1MillionReturnsFalse(self):
        self.assertTrue(isBulky(149, 149, 149))
        self.assertTrue(isBulky(100, 100, 100))


    ### sort tests ###
    def test_sort_throwsOnInvalidInput(self):
        with self.assertRaises(Exception):
            sort(0, 5, 5, 20)
        with self.assertRaises(Exception):
            sort(-3, 5, 5, 20)
        with self.assertRaises(Exception):
            sort(5, 0, 5, 20)
        with self.assertRaises(Exception):
            sort(5, -5, 5, 20)
        with self.assertRaises(Exception):
            sort(5, 5, 0, 20)
        with self.assertRaises(Exception):
            sort(5, 5, -5, 20)
        with self.assertRaises(Exception):
            sort(5, 5, 5, -20)
        with self.assertRaises(Exception):
            sort(5, 5, 5, 0)

    def test_sort_returnsStandardOnNonBulkyNonHeavy(self):
        self.assertEqual('STANDARD', sort(5, 5, 5, 5))

    def test_sort_returnsSpecialOnBulkyNonHeavy(self):
        self.assertEqual('SPECIAL', sort(150, 5, 5, 5))
        self.assertEqual('SPECIAL', sort(5, 150, 5, 5))
        self.assertEqual('SPECIAL', sort(5, 5, 150, 5))
        self.assertEqual('SPECIAL', sort(100, 100, 100, 5))
        self.assertEqual('SPECIAL', sort(100, 100, 101, 5))
        
    def test_sort_returnsSpecialOnNonBulkyHeavy(self):
        self.assertEqual('SPECIAL', sort(5, 5, 5, 50))
        
    def test_sort_returnsRejectedOnBuklyHeavy(self):
        self.assertEqual('REJECTED', sort(150, 5, 5, 50))
        self.assertEqual('REJECTED', sort(5, 150, 5, 50))
        self.assertEqual('REJECTED', sort(5, 5, 150, 50))
        self.assertEqual('REJECTED', sort(100, 100, 100, 50))
        self.assertEqual('REJECTED', sort(100, 100, 101, 50))
        

if __name__ == '__main__':
    unittest.main()
