import abc

class RateRepository(abc.ABC):

    @abc.abstractmethod
    def rate_for(self, amount):
        pass

class MockRateRepository(RateRepository):

    def rate_for(self, amount):
        return (
            0.01 if amount <= 100 else
            0.02 if amount <= 1000 else
            0.05
        )

class RepositoryFactory:

    @staticmethod
    def getMockRateRepository():
        return MockRateRepository()
