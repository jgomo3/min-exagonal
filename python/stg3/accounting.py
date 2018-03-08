class Discounter:

    def __init__(self, rate_repository):
        self.rate_repository = rate_repository

    def discount(self, amount):
        return self.rate_repository.rate_for(amount) * amount
