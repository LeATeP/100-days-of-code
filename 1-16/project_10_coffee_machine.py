MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report():
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}\n")


def receive():
    print("Please insert coins\n")
    quarter = int(input("How much quarter?: "))
    quarter *= 0.25

    return quarter


def quality_checker(menu, answer1):
    for item1 in menu[answer1]["ingredients"]:
        if resources[item1] < menu[answer1]["ingredients"][item1]:
            return False

        return True


answer = input("What would you like? (espresso, latte, cappuccino)\n: ").lower()

while answer != "end":
    if answer == "report":
        report()

    elif answer == "espresso" or "latte" or "cappuccino":
        checker = quality_checker(MENU, answer)
        change_money = receive()
        change_give = round(change_money - MENU[answer]["cost"], 3)

        if checker:
            for item in MENU[answer]["ingredients"]:
                resources[item] -= MENU[answer]["ingredients"][item]

        if checker:
            resources["money"] += MENU[answer]["cost"]
            print(f"Your change is {change_give}\n"
                  f"Here is Your latte ^*^ Enjoy!")
        else:
            print(f"Machine not having resources, Here is your money {change_money}")
    elif answer == "end":
        break
    else:
        print("you write wrong answer")

    answer = input("What would you like? (espresso, latte, cappuccino)\n: ").lower()
    print("secret commands ['report' to show resources, 'end' to end program]\n")










