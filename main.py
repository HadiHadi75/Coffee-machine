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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for  items in order_ingredients:
        if order_ingredients[items]>resources[items]:
            print("sorry insufficient ingredients")
            return False
    return True

def process_coins():
    """calculate amount of coins"""
    print("please insert coins:)")
    total=int(input("How many quarters? :"))*0.25
    total += int(input("How many dimes? :")) * 0.1
    total += int(input("How many nickles? :")) * 0.05
    total += int(input("How many pennies? :")) * 0.01
    return total

def check_transaction(money_received,drink_cost ):
   """return True if payment was succesfull, or False if it was not"""
   if money_received>= drink_cost:
       change=round(money_received-drink_cost,2)
       print((f"here is your ${change} change back"))
       global profit
       profit+=drink_cost
       return True
   else:
       print("Sorry that's not enough money.")
       return False

def make_coffee(drink_name, other_ingredients):

    """Deduct the required ingredients from the resources."""
    for item in other_ingredients:
        resources[item] -= other_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on= True
while is_on:
    question=input("What would you like? (espresso/latte/cappuccino): ")
    if question =="off":
        is_on=False
    elif question=="report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk : {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: {profit} $")

    else:
        drink=MENU[question]
        print(f"The cost of {question} is: ${drink['cost']:.2f}")  # Display drink cost
        if is_sufficient(drink["ingredients"]):
             payment=process_coins()
             if check_transaction(payment, drink["cost"]):
                 make_coffee(question, drink["ingredients"])











