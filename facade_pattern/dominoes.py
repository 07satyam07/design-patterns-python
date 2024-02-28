from pizzaadons import  PizzaAdons
from pizza_builder import  PizzaBuilder


class Dominoes:
    _pizzaAdon=PizzaAdons.get_instance()

    def __init__(self):
        self.pizzaBuilder=PizzaBuilder()
        self.pizzAdons=self._pizzaAdon

    def view(self):
        return  self.pizzAdons.get_menu()

    def build_pizza(self):
        return PizzaBuilder()
