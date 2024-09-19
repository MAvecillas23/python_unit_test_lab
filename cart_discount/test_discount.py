import unittest 
from unittest import TestCase
from price_discount import discount
from python_unit_test_lab.cart_discount import price_discount


class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # more unit tests here. Each test should test one scenario
    def test_list_of_less_than_three_prices(self):
        prices = [1,4]
        self.assertEqual(0, discount(prices))

    def test_list_of_one_price(self):
        prices = [4]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_zero_price(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_in_string(self):
        prices = ['cat', 'star', 'dog']
        with self.assertRaises(TypeError):
            price_discount.discount(prices)

    def test_list_in_negative_numbers(self):
        prices = [-4, -2, -10]
        self.fail('Finish')

    def test_zero_in_price_list(self):
        prices = 0
        self.fail('finish')


    def test_float_point_in_price_list(self):
        prices = [3.4, 2.6, 10.4]
        self.fail('finish')



if __name__ == '__main__':
    unittest.main()