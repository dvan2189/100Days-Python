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
    "water": 3000,
    "milk": 1000,
    "coffee": 500,
}

is_on = True
profit = 0

def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] = resources[item] - order_ingredient[item]
    print(f"Here is your drink {drink_name}. Enjoy")

def check_ingredient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    total = 0
    print("Please insert some coin: ")
    quarter = int(input("How many quarter?: "))*0.25
    dime = int(input("How many dime?: "))*0.1
    nickel = int(input("How many nickel?: "))*0.05
    penny = int(input("How many penny?: "))*0.01
    total = quarter + dime + nickel + penny
    return total

def check_transaction(money_received, drink_cost):
    if (money_received >= drink_cost):
        change = round(money_received - drink_cost,2)
        print(f"Here is your change {change}")
        global profit
        profit = profit + drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refund")
        return False

while(is_on):
    choose = input("What would you like? (espresso/latte/cappuccino): ")
    if choose == "off":
        is_on = False
    elif choose == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink  = MENU[choose]
        if(check_ingredient(drink["ingredients"])):
            payment = process_coin()
            if(check_transaction(payment,drink["cost"])):
                make_coffee(choose,drink["ingredients"])


