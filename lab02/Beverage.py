# Beverage.py

class Beverage:
    def __init__(self, ounces = 12, price = 5.0):
        self.ounces = int(ounces)
        self.price = float(price)
        
    def updateOunces(self, newOunces):
        self.ounces = int(newOunces)
    
    def updatePrice(self, newPrice):
        self.price = float(newPrice)

    def getOunces(self):
        return int(self.ounces)
    
    def getPrice(self):
        return self.price
    
    def getInfo(self):
        return "{} oz, ${:.2f}".format(self.ounces, self.price)
    
    def __eq__(self, rhs):
        return self.ounces == rhs.ounces and self.price == rhs.price
    
    def __add__(self, rhs):
        return Beverage(self.ounces + rhs.ounces, self.price + rhs.price)