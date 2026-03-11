# SpecialtyTea.py

from Tea import Tea

class SpecialtyTea(Tea):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name

        if self.size == "S":
            price = 12.0
        elif self.size == "M":
            price = 16.0
        else:
            price = 20.0
        self.price = price

    def getTeaDetails(self):
        output = "SPECIALTY TEA\nSize: {}\nName: {}\nPrice: ${:.2f}\n".format(self.size, self.name, self.price)
        return output
