# TeaOrder.py

from CustomTea import CustomTea
from SpecialtyTea import SpecialtyTea

class TeaOrder:
    def __init__(self, distance):
        self.teas = []
        self.distance = distance
    
    def addTea(self, tea):
        self.teas.append(tea)

    def getOrderDescription(self):
        output = f"******\nShipping Distance: {self.distance} miles\n"
        totalPrice = 0

        for tea in self.teas:
            output += tea.getTeaDetails() + "\n----\n"
            totalPrice += tea.getPrice()
        
        output += f"TOTAL ORDER PRICE: ${totalPrice:.2f}\n******\n"

        return output

