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


profit = 0
is_on = True


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False otherwise"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    """Returns True when the payment is accepted, False otherwise"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


while is_on:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    request = input("What would you like? (espresso/latte/cappuccino) ").lower()
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if request == 'off':
        print("Coffee Machine Off")
        is_on = False
    elif request == f"report":
        # TODO: 3. Print report.
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[request]
        # TODO: 4. Check resources sufficient?
        if is_resource_sufficient(drink["ingredients"]):
            # TODO: 5. Process coins.
            payment = process_coins()
            # TODO: 6. Check transaction successful?
            if is_transaction_successful(payment, drink["cost"]):
                # TODO: 7. Make Coffee.
                make_coffee(request, drink["ingredients"])











