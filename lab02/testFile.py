# testFile.py

from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder


class Test_Beverage():

    def test_updateOunces(self):
        b1 = Beverage(12, 5.0)
        b1.updateOunces(45)
        assert b1.getOunces() == 45 

    def test_updatePrice(self):
        b1 = Beverage(12, 5.0)
        b1.updatePrice(3)
        assert b1.getPrice() == 3.0

    def test_getOunces(self):
        b1 = Beverage(ounces = 5, price = 8.0)
        assert b1.getOunces() == 5

    def test_getPrice(self):
        b1 = Beverage(12, 5.0)
        assert b1.getPrice() == 5.0

    def test_getInfo(self): 
        b1 = Beverage(12, 5.0)
        assert b1.getInfo() == "{} oz, ${:.2f}".format(12, 5.0)


class Test_Coffee():

    def test_updateOunces(self):
        b1 = Coffee(12, 5.0, "Pour-over")
        b1.updateOunces(45)
        assert b1.getOunces() == 45 

    def test_updatePrice(self):
        b1 = Coffee(12, 5.0, "Pour-over")
        b1.updatePrice(3)
        assert b1.getPrice() == 3.0

    def test_getOunces(self):
        b1 = Coffee(ounces = 5, price = 8.0, style = "Pour-over")
        assert b1.getOunces() == 5

    def test_getPrice(self):
        b1 = Coffee(12, 5.0, "Pour-over")
        assert b1.getPrice() == 5.0

    def test_getInfo(self):
        c1 = Coffee(12, 5.0, "Pour-over")
        assert c1.getInfo() == "Pour-over Coffee, 12 oz, $5.00"

class Test_FruitJuice():
    def test_updateOunces(self):
        b1 = FruitJuice(12, 5.0, ["Orange"])
        b1.updateOunces(45)
        assert b1.getOunces() == 45 

    def test_updatePrice(self):
        b1 = FruitJuice(12, 5.0, ["Orange"])
        b1.updatePrice(3)
        assert b1.getPrice() == 3.0

    def test_getOunces(self):
        b1 = FruitJuice(ounces = 5, price = 8.0, fruits = ["Orange"])
        assert b1.getOunces() == 5

    def test_getPrice(self):
        b1 = FruitJuice(12, 5.0, ["Orange"])
        assert b1.getPrice() == 5.0

    def test_getInfo(self):
        b1 = FruitJuice(12, 5.0, ["Orange"])
        assert b1.getInfo() == "Orange Juice, 12 oz, $5.00"

        b2 = FruitJuice(12, 5.0, ["Orange", "Mango"])
        assert b2.getInfo() == "Orange/Mango Juice, 12 oz, $5.00"

class Test_DrinkOrder():
    def test_addBeverage(self):
        order = DrinkOrder()
        b1 = Beverage(12, 5.0)
        order.addBeverage(b1)

        assert order.getTotalOrder() == "Order Items:\n* 12 oz, $5.00\nTotal Price: $5.00"

    def test_getTotal(self):
        def test_addBeverage(self):
            order = DrinkOrder()
            b1 = Beverage(12, 5.0)
            order.addBeverage(b1)

            assert order.getTotalOrder() == "Order Items:\n* 12 oz, $5.00\nTotal Price: $5.00"
