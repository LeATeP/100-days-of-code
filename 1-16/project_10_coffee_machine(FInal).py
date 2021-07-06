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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${money}\n")


def stock_check(required_items):
    in_stock = True
    for item in required_items:
        if required_items[item] > resources[item]:
            in_stock = False
    return in_stock


def receive():
    # Return coins
    print("Please insert coins\n")
    quarter = int(input("How much quarter?: "))
    quarter *= 0.25

    return quarter


def sort_stock(required):
    for item in required:
        resources[item] -= required[item]


is_on = True
while is_on:
    choice = input("espresso, latte, or cappuccino: \n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        report()
    elif choice == "espresso" or "latte" or "cappuccino":
        drink = MENU[choice]
        if stock_check(drink["ingredients"]):
            payment = receive()
            if payment >= drink["cost"]:
                payment -= drink["cost"]
                sort_stock(drink["ingredients"])
                money += drink["cost"]

                print(f"Here is your Coffee ^*^\n"
                      f"Here is your change {payment}")
            else:
                print(f"Money is insuficient, here is your money {payment}")
        else:
            print("Out of stock")














