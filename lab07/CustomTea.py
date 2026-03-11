# CustomTea.py

from Tea import Tea

class CustomTea(Tea):
    def __init__(self, size, base):
        super().__init__(size)
        self.base = base
        self.flavors = []
        if self.size == "S":
            price = 10.0
        elif self.size == "M":
            price = 15.0
        else:
            price = 20.0
        self.price = price

    def setBase(self, base):
        self.base = base
        return self.base
    
    def getBase(self):
        return self.base
    
    def addFlavor(self, flavor):
        self.flavors.append(flavor)
        if self.size == "S":
            price = 10.0 + 0.25 * len(self.flavors)
        elif self.size == "M":
            price = 15.0 + 0.50 * len(self.flavors)
        else:
            price = 20.0 + 0.75 * len(self.flavors)
        self.price = price
    
    def getTeaDetails(self):
        flavorList = ""
        if len(self.flavors) > 0:
            flavorList += "\n"
            for flav in self.flavors:
                flavorList += "\t+ " + flav + "\n"
            flavorList = flavorList[:len(flavorList)-1]

        output = "CUSTOM TEA\nSize: {}\nBase: {}\nFlavors:{}\nPrice: ${:.2f}\n".format(self.size, self.base, flavorList, self.price)
        return output

