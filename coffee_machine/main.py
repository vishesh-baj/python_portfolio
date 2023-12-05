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
    "money": 0
}

machine_on = True


def prompt_user():
    user_input = input("What would you like to have? espresso/cappuccino/latte?: ")
    return user_input


def print_report():
    for key, value in resources.items():
        print(f"{key}: {value}")


def check_resources(drink_type):
    resources_required = MENU[drink_type]["ingredients"]
    resources_present = resources
    cost = MENU[drink_type]["cost"]
    for key, value in resources_required.items():
        if resources_present[key] - value <= 0:
            print(f"Insufficient Material : {key}")
            return 0
        else:
            resources_present[key] -= value
            return cost
    print(resources_present)


def process_coins(total_amount):
    # quarters = 0.25$
    quarters = int(input("How many quarters?: "))
    # dimes = 0.10$
    dimes = int(input("How many dimes?: "))
    # nickels = 0.05$
    nickels = int(input("How many nickels?: "))
    # pennies = 0.01$
    pennies = int(input("How many pennies?: "))

    total_coins_inserted = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    if total_coins_inserted < total_amount:
        print("Sorry, you cannot purchase the drink due to insufficient amount provided, Money refunded")
        return
    else:
        total_change = total_coins_inserted - total_amount
        resources["money"] += total_amount
        print(f"Here is your change of {round(total_change, 2)}")
        print_report()


while machine_on:
    user_inp = prompt_user()
    if user_inp == "report":
        print_report()
    elif user_inp == "off":
        print("Turning off the Machine")
        machine_on = False
    elif user_inp == "latte" or user_inp == "espresso" or user_inp == "cappuccino":
        drink_cost = check_resources(user_inp)
        if drink_cost > 0:
            process_coins(drink_cost)


















