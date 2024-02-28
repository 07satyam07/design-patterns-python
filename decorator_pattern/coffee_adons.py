from coffee import Coffee

class SimpleCoffee(Coffee):
    def cost(self):
        return 5

class Milk(Coffee):
    def __init__(self,coffee) -> None:
        self._coffee=coffee
    
    def cost(self):
        return self._coffee.cost()+3

class Sugar(Coffee):
    def __init__(self,coffee) -> None:
        self._coffee=coffee
    
    def cost(self):
        return self._coffee.cost()+2