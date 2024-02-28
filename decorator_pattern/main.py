from addons_enum import CoffeeAdonsOptions
from coffee_cost import CoffeeCost


addons=[CoffeeAdonsOptions.MILK,CoffeeAdonsOptions.SUGAR]

c1=CoffeeCost()
print(c1.get_cost(addons))

addons=[CoffeeAdonsOptions.MILK]
c2=CoffeeCost()
print(c2.get_cost(addons))