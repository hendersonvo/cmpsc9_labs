# Item.py

class Item:
    ''' Define a grocery item. Define the Item object by:
        * upc - 12 digit int
        * category - str
        * name - str
        * price - float '''
    
    def __init__(self, upc = None, category = None, name = None, price = None):
        if type(upc) == int and len(str(upc)) == 12:
            self.upc = upc
        else:
            self.upc = None
        if type(category) == str:
            self.category = category.upper()
        else:
            self.category = None
        if type(name) == str:
            self.name = name.upper()
        else:
            self.name = None
        if type(price) == float or type(price) == int:
            self.price = float(price)
        else:
            self.price = None
    
    def setUpc(self, upc):
        if type(upc) == int and len(str(upc)) == 12:
            self.upc = upc

    def setCategory(self, category):
        if type(category) == str:
            self.category = category.upper()

    def setName(self, name):
        if type(name) == str:
            self.name = name.upper()

    def setPrice(self, price):
        if type(price) == float or type(price) == int:
            self.price = float(price)

    def toString(self):
        return f"UPC: {self.upc}, Category: {self.category}, Name: {self.name}, Price: ${self.price:.2f}"
