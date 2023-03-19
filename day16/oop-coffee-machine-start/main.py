from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()
coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()

continue_flag = True


def order(choice):
    drink = menu_obj.find_drink(user_input)
    # print(drink)
    check_resource = coffee_maker_obj.is_resource_sufficient(drink)
    check_money = money_machine_obj.make_payment(drink.cost)
    if check_resource and check_money:
        coffee_maker_obj.make_coffee(drink)


while continue_flag:
    user_input = input(f"What would you like? ({menu_obj.get_items()}): ").lower()
    if user_input == "off":
        continue_flag = False
    elif user_input == "report":
        coffee_maker_obj.report()
        money_machine_obj.report()
    else:
        order(user_input)
