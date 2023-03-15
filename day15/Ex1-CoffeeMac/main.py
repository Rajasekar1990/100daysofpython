MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters=int(input("how many quarters: "))*0.25
    dimes=int(input("how many dimes: "))*0.10
    nickles=int(input("how many nickles: "))*0.05
    pennies=int(input("how many pennies: "))*1
    amount=quarters+dimes+nickles+pennies
    return amount

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money_remaining
        money_remaining += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

money_remaining=0
promptflag=True
while promptflag:
    order=input("What would you like? (espresso/latte/cappuccino): ")
    if promptflag== "off":
        promptflag=False
    elif (order == "report"):
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} g")
        print(f"Money: ${money_remaining}")
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            money = process_coins()
            if is_transaction_successful(money, drink["cost"]):
                make_coffee(order, drink["ingredients"])






