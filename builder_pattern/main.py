class Pizza:
    def __init__(self):
        self.crust=""
        self.toppings=[]

    def __str__(self):
        return f"{self.crust} crust pizza with {','.join(self.toppings)} toppings"

class PizzaBuilder:
    def __init__(self):
        self.pizza=Pizza()

    def add_toppings(self,topping):
        self.pizza.toppings.append(topping)
        return self

    def add_crust(self,crust):
        self.pizza.crust=crust
        return self

    def build(self):
        return self.pizza

pizza=PizzaBuilder().add_crust("thin").add_toppings("tomato").add_toppings("onion").build()

print(pizza)