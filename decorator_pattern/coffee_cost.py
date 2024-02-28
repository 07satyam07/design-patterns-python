from coffee_adons import SimpleCoffee,Milk,Sugar
from addons_enum import CoffeeAdonsOptions

class CoffeeCost:
    def __init__(self,addons=[]) -> None:
        self.coffee=SimpleCoffee()
    
    def get_cost(self,addons):
        print(addons)
        for addon in addons:
            if addon==CoffeeAdonsOptions.MILK:
                self.coffee=Milk(self.coffee)
            elif addon==CoffeeAdonsOptions.SUGAR:
                self.coffee=Sugar(self.coffee)
        return self.coffee.cost()


