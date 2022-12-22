from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
payment = MoneyMachine()
espresso = MenuItem(name="espresso", water=50, milk=0, coffee=24, cost=1.5)
latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
cappuccino = MenuItem(name="cappuccino", water=250,  milk=50, coffee=24, cost=3)
menu = Menu()

brewing_on = True
while brewing_on:

    order = input(f"Choose your drink {menu.get_items()}: ")
    if order == "report":
        coffee_machine.report()
        payment.report()
    elif order == "off":
        brewing_on = False
    else:
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink):
            if payment.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
            else:
                brewing_on = False


