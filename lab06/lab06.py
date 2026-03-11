# lab06.py

from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2

        leftlist = apartmentList[:mid]
        rightlist = apartmentList[mid:]

        mergesort(leftlist)
        mergesort(rightlist)

        i = 0
        j = 0
        k = 0

        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                apartmentList[k] = leftlist[i]
                i += 1
            else:
                apartmentList[k] = rightlist[j]
                j += 1
            k += 1

        while i < len(leftlist):
            apartmentList[k] = leftlist[i]
            i += 1
            k += 1
        
        while j < len(rightlist):
            apartmentList[k] = rightlist[j]
            j += 1
            k += 1

def ensureSortedAscending(apartmentList):
    for i in range(len(apartmentList) - 1):
        if apartmentList[i] > apartmentList[i + 1]:
            return False
    return True

def getBestApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[0].getApartmentDetails()

def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[len(apartmentList) - 1].getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    mergesort(apartmentList)
    output = ""
    for i in apartmentList:
        if i.getRent() <= budget:
            output += i.getApartmentDetails() + "\n"
    output = output[:len(output)-1] # trim the final newline char
    return output
