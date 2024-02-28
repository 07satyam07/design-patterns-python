from dominoes import  Dominoes


order=Dominoes()
print(order.view())

pizza=order.build_pizza()

print(pizza.add_crust("thin").add_toppings("tomato").add_toppings("onions").build())
