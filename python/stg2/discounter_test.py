import unittest
import accounting

fixtures = [
    { "amount": amount, "discount": discount }
    for amount, discount in [
            (100, 5),
            (200, 10),
    ]
]


class TestDiscounter(unittest.TestCase):

    def test_discount(self):
        discounter = accounting.Discounter()
        for fixture in fixtures:
            self.assertEqual(
                discounter.discount(fixture["amount"]),
                fixture["discount"]
            )
