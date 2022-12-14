from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    coffees = menu.get_items()
    order = input(f"What would you like? ({coffees})").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
    else:
        right_order = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(right_order) and money_machine.make_payment(right_order.cost):
            coffee_maker.make_coffee(right_order)


            # money_machine.make_payment(right_order.cost)

        # else:
        #     print("Sorry that's not enough money. Money refunded.")



# coffee_maker.report()
# coffee_maker.is_resource_sufficient(latte)