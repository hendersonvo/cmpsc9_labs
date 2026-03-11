# Coffee.py

from Beverage import Beverage

class Coffee(Beverage):
    def __init__(self, ounces = 12, price = 5.0, style = "Pour-over"):
        super().__init__(ounces, price)
        self.style = str(style)

    def getInfo(self):
        return "{} Coffee, ".format(self.style) + super().getInfo()
    
    def __eq__(self, rhs):
        return super().__eq__(rhs) and self.style == rhs.style
