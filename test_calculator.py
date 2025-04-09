import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,3), 6)
        self.assertEqual(add(-3,3), 0)
        self.assertEqual(add(-3,-3), -6)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(4,3), 1)
        self.assertEqual(subtract(-3,-3), 0)
        self.assertEqual(subtract(-3, 3), -6)
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        pass

    def test_divide(self): # 3 assertions
        pass
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)
        #call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 1), 1)
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(1,1), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,1)
        # use same technique from test_divide_by_zero
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        pass

    def test_hypotenuse(self): # 3 assertions
        pass

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        pass
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()