# testFile.py

from Apartment import Apartment
from lab06 import *

def test_apartment_methods():
    a0 = Apartment(1000, 100, "average")
    assert a0.getRent() == 1000
    assert a0.getMetersFromUCSB() == 100
    assert a0.getCondition() == "average"
    assert a0.getApartmentDetails() == "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}"\
        .format(1000, 100, "average")

def test_eq_apartment():
    a1 = Apartment(1200, 200, "average")
    a2 = Apartment(1200, 200, "average")
    assert a1 == a2
    a2 = Apartment(1200, 200, "bad")
    assert a1 != a2

def test_gt_apartment():
    a1 = Apartment(1200, 200, "average")
    a2 = Apartment(1000, 200, "average")
    assert a1 > a2
    a2 = Apartment(1400, 200, "average")
    assert a2 > a1
    a1 = Apartment(1400, 300, "average")
    assert a1 > a2
    a2 = Apartment(1400, 400, "average")
    assert a2 > a1
    a1 = Apartment(1400, 400, "bad")
    assert a1 > a2
    a1 = Apartment(1400, 400, "excellent")
    assert a2 > a1

def test_lt_apartment():
    a1 = Apartment(1200, 200, "average")
    a2 = Apartment(1000, 200, "average")
    assert a2 < a1
    a2 = Apartment(1400, 200, "average")
    assert a1 < a2
    a1 = Apartment(1400, 300, "average")
    assert a2 < a1
    a2 = Apartment(1400, 400, "average")
    assert a1 < a2
    a1 = Apartment(1400, 400, "bad")
    assert a2 < a1
    a1 = Apartment(1400, 400, "excellent")
    assert a1 < a2

def test_mergesort():
    alist = [9,8,7,6,5,4,3,2,1]
    blist = [1,1,1,1,1,1,1,1,1]
    clist = [1,9,2,8,3,7,4,6,5]
    dlist = [-1,-2,-3,-4,-5,-6,-7,-8,-9]
    elist = [-1,-2,1,2,0]
    mergesort(alist)
    mergesort(blist)
    mergesort(clist)
    mergesort(dlist)
    mergesort(elist)
    assert alist == [1,2,3,4,5,6,7,8,9]
    assert blist == [1,1,1,1,1,1,1,1,1]
    assert clist == [1,2,3,4,5,6,7,8,9]
    assert dlist == [-9,-8,-7,-6,-5,-4,-3,-2,-1]
    assert elist == [-2,-1,0,1,2]

def test_ensureSortedAscending():
    alist = [1,2,3,4]
    blist = [1,2,3,0]
    clist = [-1,0,1,10]
    dlist = [1,-2,3,-4]
    assert ensureSortedAscending(alist) == True
    assert ensureSortedAscending(blist) == False
    assert ensureSortedAscending(clist) == True
    assert ensureSortedAscending(dlist) == False

def test_getBestApartment():
    a1 = Apartment(1200, 200, "average")
    a2 = Apartment(1000, 200, "average")

    alist = [a1, a2]

    assert getBestApartment(alist) == Apartment(1000, 200, "average").getApartmentDetails()

def test_getWorstApartment():

    a1 = Apartment(1200, 200, "average")
    a2 = Apartment(1000, 200, "average")

    alist = [a1, a2]

    assert getWorstApartment(alist) == Apartment(1200, 200, "average").getApartmentDetails()

def test_getAffordableApartments():
    a1 = Apartment(2000, 200, "average")
    a2 = Apartment(1800, 200, "average")
    a3 = Apartment(1600, 200, "average")
    a4 = Apartment(1400, 200, "average")
    a5 = Apartment(1200, 200, "average")

    alist = [a1, a2, a3, a4, a5]
    assert getAffordableApartments(alist, 1200) == Apartment(1200, 200, "average").getApartmentDetails()
    assert getAffordableApartments(alist, 1500) == Apartment(1200, 200, "average").getApartmentDetails() + "\n" + Apartment(1400, 200, "average").getApartmentDetails()
