class CurrencyConverter:

    _instance=None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance=cls()
        return cls._instance

    def __init__(self):
        self.coverter={
            "dollar":1,
            "pound":0.83,
            "yen":0.75
        }

    def convert_to_dollars(self,currency,amount):
        return self.coverter[currency]*amount


cc=CurrencyConverter()