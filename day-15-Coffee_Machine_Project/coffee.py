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
    "money": 0,
}

def userchoice():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice

keepLooping = True

while keepLooping:

    def coffeemachine():
        choice = userchoice()

        if choice == "off":
            exit()

        elif choice == "report":
            print(f"Water: {resources["water"]}ml  ")
            print(f"Milk: {resources["milk"]}ml  ")
            print(f"Coffee: {resources["coffee"]}g  ")
            print(f"Money: {resources["money"]}$  ")

        elif choice == "espresso":
            if resources["water"]  <  MENU[choice]["ingredients"]["water"]:
                print("Sorry, there is not enough water")
                coffeemachine()
            elif resources["coffee"]  <  MENU[choice]["ingredients"]["coffee"]:
                print("Sorry, there is not enough coffee")
                coffeemachine()

        elif choice == "latte":
            if resources["water"]  <  MENU[choice]["ingredients"]["water"]:
                print("Sorry, there is not enough water")
                coffeemachine()
            elif resources["coffee"]  <  MENU[choice]["ingredients"]["coffee"]:
                print("Sorry, there is not enough coffee")
                coffeemachine()
            elif resources["milk"] < MENU[choice]["ingredients"]["milk"]:
                print("Sorry, there is not enough milk")
                coffeemachine()

        elif choice == "cappuccino":
            if resources["water"]  <  MENU[choice]["ingredients"]["water"]:
                print("Sorry, there is not enough water")
                coffeemachine()
            elif resources["coffee"]  <  MENU[choice]["ingredients"]["coffee"]:
                print("Sorry, there is not enough coffee")
                coffeemachine()
            elif resources["milk"] < MENU[choice]["ingredients"]["milk"]:
                print("Sorry, there is not enough milk")
                coffeemachine()




            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            totalInserted = (quarters * 25 + dimes * 10 + nickles * 5 + pennies) / 100
            print(MENU[choice]["cost"])


            if totalInserted >= MENU[choice]["cost"]:
                resources["money"] += MENU[choice]["cost"]
                if totalInserted > MENU[choice]["cost"]:
                    print(f"Here is your change: ${totalInserted - MENU[choice]["cost"]}")
            elif totalInserted < MENU[choice]["cost"]:
                print("Sorry, not enough money. Money refunded.")

            print(f"Here is your {choice}. Enjoy!")
            coffeemachine()

    coffeemachine()
