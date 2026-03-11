# Store.py

from Item import Item

class Store:
    ''' Define a store object. A Store contains a dictionary structure where the
        keys will be a str representing an Item's category and the
        values will be a list of Item objects that the Store contains.'''

    def __init__(self):
        self.stores = {}        # creates an empty store

    def addItem(self, item):    # add an Item to the store if it doesn't already exist
        if self.stores.get(item.category) == None:
            self.stores[item.category] = [item]     # if the store doesn't have this category, add the Item
        elif not item in self.stores[item.category]:
            self.stores[item.category].append(item) # else, if this item is not in the list for this category, add it
    
    def removeItem(self, item):
        if item in self.stores[item.category]:
            self.stores[item.category].remove(item) # if the item is in a category list, remove it (items are unique)

    def removeCategory(self, category):
        
        category = category.upper()

        if category in self.stores:
            self.stores.pop(category)       # if a category exists in a store, remove it

    def getItems(self, category):
        ''' Print a string containing all Items of a certain category. One line per item. '''

        category = category.upper()

        if self.stores.get(category) == None:
            return ""

        else:
            catString = ""              # create a new string

            for item in self.stores[category]:
                if item == self.stores[category][len(self.stores[category])-1]:
                    catString = catString + item.toString()         # if item is the last in the category list, append to string with no new line 
                else:
                    catString = catString + item.toString() + "\n"  # otherwise, append to string with a new line
            
            return catString
        
    def doesItemExist(self, item):
        for category in self.stores:
            if item in self.stores[category]:
                return True
        return False
    
    def countDollarItems(self):
        ''' Returns an int representing the number of items that are less than or equal to 1 dollar '''
    
        itemCount = 0

        for category in self.stores:
            for item in self.stores[category]:
                if item.price <= 1:
                    itemCount += 1
        return itemCount