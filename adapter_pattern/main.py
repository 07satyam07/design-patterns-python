from currencyconvertor import cc
from database import  db

class Adapter:
    def __init__(self):
        self.cc=cc.get_instance()
        self.db=db.get_instance()

    def adapt(self,currency,amount):
        return self.cc.convert_to_dollars(currency,amount)

    def write(self,currency,amount):
        self.db.write_currency(self.adapt(currency,amount))


adapter=Adapter()
adapter.write("pound",48)