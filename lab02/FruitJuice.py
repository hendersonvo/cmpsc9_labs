# FruitJuice.py

from Beverage import Beverage

class FruitJuice(Beverage):
    def __init__(self, ounces=12, price=5, fruits = ["Orange"]):
        super().__init__(ounces, price)
        self.fruits = fruits

    def getInfo(self):
        fcombo = ""

        for f in self.fruits: 
            fcombo += f
            if f == self.fruits[len(self.fruits)-1]:
                break
            fcombo += "/"
        
        return "{} Juice, ".format(fcombo) + super().getInfo()
    
    def __eq__(self, rhs):
        if len(self.fruits) != len(rhs.fruits):
            return False
        else:
            for f in self.fruits:
                if not f in rhs.fruits:
                    return False
        
        return super().__eq__(rhs)