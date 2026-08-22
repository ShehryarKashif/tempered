import unittest
from cart import cart_total

class TestCart(unittest.TestCase):
    def test_whole_dollar_items(self):
        self.assertEqual(cart_total([(2, 5.00)]), 10.00)

    def test_cents_items(self):
        self.assertEqual(cart_total([(3, 0.10), (2, 0.20)]), 0.70)
