import unittest
from hw_shop import purchase, retry_purchase, ThreeFailedAttempts


# prices = {"Denim Jacket": 65, "Sunglasses": 20, "Trainers": 150}

class TestPurchase(unittest.TestCase):
    def test_purchase(self):
        self.assertEqual(True, purchase(item="Sunglasses", customer_balance=100))

    def test_purchase_with_not_enough_money(self):
        self.assertFalse(purchase(item="Trainers", customer_balance=100))

    def test_purchase_with_negative_money(self):
        self.assertEqual(False, purchase(item="Denim Jacket", customer_balance=-50))

    def test_purchase_with_just_enough_money(self):
        self.assertTrue(purchase(item="Denim Jacket", customer_balance=150))


class TestRetryPurchase(unittest.TestCase):
    def test_retry_purchase_too_many_attempts(self):
        with self.assertRaises(ThreeFailedAttempts):
            retry_purchase(item="Trainers", customer_balance=100, attempts=3),


if __name__ == '__main__':
    unittest.main()

