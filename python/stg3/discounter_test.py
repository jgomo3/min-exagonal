import unittest
import accounting
import accounting_storage

fixtures = [
    { "amount": amount, "discount": discount }
    for amount, discount in [
            (100, 1),
            (200, 4),
            (1000, 20),
            (1100, 55)
    ]
]


class TestDiscounter(unittest.TestCase):

    def test_discount(self):
        rate_repository = accounting_storage.RepositoryFactory.getMockRateRepository()
        discounter = accounting.Discounter(rate_repository)
        for fixture in fixtures:
            self.assertEqual(
                discounter.discount(fixture["amount"]),
                fixture["discount"]
            )
