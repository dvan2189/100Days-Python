from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Initilize the object 
money_machine = MoneyMachine()
menu = Menu()
#menu_item = MenuItem()
coffee_maker = CoffeeMaker()

coffee_maker.report()
money_machine.report()

is_on = True
while is_on:
	option = menu.get_items()
	choose = input(f"What would you like? ({option}): ")
	if choose =="off":
		is_on = False
	elif choose == "report":
		coffee_maker.report()
		money_machine.report()
	else:
		drink = menu.find_drink(choose)
		if coffee_maker.is_resource_sufficient(drink):
			if money_machine.make_payment(drink.cost):
				coffee_maker.make_coffee(drink)
				
