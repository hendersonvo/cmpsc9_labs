# DrinkOrder.py

from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice

class DrinkOrder:
    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        price = 0
        for d in self.drinks:
            price += d.getPrice()
        
        order = "Order Items:\n"
        for i in self.drinks:
            order += "* " + i.getInfo() + "\n"        
        order += "Total Price: ${:.2f}".format(price)

        return order

# d = DrinkOrder()

# print(d.drinks)

# c = Coffee()
# oj = FruitJuice()

# d.addBeverage(c)
# d.addBeverage(oj)

# print(d.getTotalOrder())