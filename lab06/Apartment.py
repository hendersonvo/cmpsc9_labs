# Apartment.py

class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent
    
    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    
    def getCondition(self):
        return self.condition
    
    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}"\
        .format(self.rent, self.metersFromUCSB, self.condition)
    
    def __eq__(self, rhs):
        if self.rent == rhs.rent and self.metersFromUCSB == rhs.metersFromUCSB and self.condition == rhs.condition:
            return True
        return False
    
    def __gt__(self, rhs):
                
        if self.rent > rhs.rent:
            return True
        elif self.rent < rhs.rent:
            return False
        elif self.rent == rhs.rent:
            if self.metersFromUCSB > rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB == rhs.metersFromUCSB:
                if self.condition == "excellent":
                    return False
                elif self.condition == "average":
                    if rhs.condition == "excellent":
                        return True
                    else:
                        return False
                else:
                    if rhs.condition == "bad":
                        return False
                    else:
                        return True
        return False
    
    def __lt__(self, rhs):

        if self.rent < rhs.rent:
            return True
        elif self.rent > rhs.rent:
            return False
        elif self.rent == rhs.rent:
            if self.metersFromUCSB < rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB == rhs.metersFromUCSB:
                if self.condition == "bad":
                    return False
                elif self.condition == "average":
                    if rhs.condition == "bad":
                        return True
                    else:
                        return False
                else:
                    if rhs.condition == "excellent":
                        return False
                    else:
                        return True
        return False