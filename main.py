from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True


while is_on:
    order= input(f"what would you like to ({menu.get_items()}) : ")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        is_resources_enough = coffee_maker.is_resource_sufficient(drink)
        if is_resources_enough:
           coins= money_machine.make_payment(drink.cost)
           if coins:
                coffee_maker.make_coffee(drink)
                

            
               
           





 




