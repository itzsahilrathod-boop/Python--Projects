MENU_DATA = {
    "espresso": {
        "requirements": {"water": 50, "coffee": 18},
        "price": 1.5,
    },
    "latte": {
        "requirements": {"water": 200, "milk": 150, "coffee": 24},
        "price": 2.5,
    },
    "cappuccino": {
        "requirements": {"water": 250, "milk": 100, "coffee": 24},
        "price": 3.0,
    }
}

machine_supplies = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
vault = 0.0


def check_stock(drink_name):
    recipe = MENU_DATA[drink_name]["requirements"]
    for item in recipe:
        if recipe[item] > machine_supplies.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def collect_payment():
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        return quarters + dimes + nickels + pennies
    except ValueError:
        print("Invalid input. You must enter numbers.")
        return 0.0


def process_transaction(inserted_funds, drink_cost):
    if inserted_funds >= drink_cost:
        change = round(inserted_funds - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global vault
        vault += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def prepare_coffee(drink_name):
    recipe = MENU_DATA[drink_name]["requirements"]
    for item in recipe:
        machine_supplies[item] -= recipe[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_running = True

while is_running:
    user_input = input("What would you like? (1 for Espresso, 2 for Latte, 3 for Cappuccino): ").strip().lower()

    if user_input in ["1", "espresso"]:
        choice = "espresso"
    elif user_input in ["2", "latte"]:
        choice = "latte"
    elif user_input in ["3", "cappuccino"]:
        choice = "cappuccino"
    elif user_input == "off":
        choice = "off"
    elif user_input == "report":
        choice = "report"
    else:
        print("Invalid selection. Please enter 1, 2, or 3.")
        continue  # This forces the loop to skip the rest of the code and ask for input again

    if choice == "off":
        is_running = False
    elif choice == "report":
        print(f"Water: {machine_supplies['water']}ml")
        print(f"Milk: {machine_supplies['milk']}ml")
        print(f"Coffee: {machine_supplies['coffee']}g")
        print(f"Money: ${vault:.2f}")
    elif choice in MENU_DATA:
        if check_stock(choice):
            payment = collect_payment()
            if payment > 0:
                if process_transaction(payment, MENU_DATA[choice]["price"]):
                    prepare_coffee(choice)