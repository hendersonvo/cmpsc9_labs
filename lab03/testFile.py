# testFile.py

from lab03 import *

def test_integerDivision():
    assert integerDivision(4,4) == 1
    assert integerDivision(5,4) == 1
    assert integerDivision(3,4) == 0

def test_collectEvenInts():
    assert collectEvenInts([1,2,3,4,5,6,7,8,9,0]) == [2,4,6,8,0]
    assert collectEvenInts([2,2,2,2,2,2,2,2,2,2]) == [2,2,2,2,2,2,2,2,2,2]
    assert collectEvenInts([22,55,77,88,103,104]) == [22,88,104]
    assert collectEvenInts([]) == []

def test_countVowels():
    assert countVowels("uu ii ii aa") == 8
    assert countVowels("UU II II AA") == 8
    assert countVowels("12345") == 0
    assert countVowels("AeIoU") == 5
    assert countVowels("") == 0
    assert countVowels("123jko") == 1

def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("Pop") == "poP"
    assert reverseString("1234567890") == "0987654321"
    assert reverseString("") == ""

def test_removeSubString():
    assert removeSubString("pop", "pop") == ""
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("this is a sentence", " ") == "thisisasentence"
    assert removeSubString("string", "what") == "string"