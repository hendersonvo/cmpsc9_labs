# lab03.py

def integerDivision(n, k):
    '''
    Return the quotient n // k
    
    :param n: is an int
    :param k: is an int
    '''

    if n < k:
        return 0
    return 1 + integerDivision(n - k, k)

def collectEvenInts(listOfInt):
    '''
    Retern a list containing only even values
    
    :param listOfInt: is a list of positive integer values
    '''
    if len(listOfInt) == 0:
        return []
    
    i = listOfInt.pop()
    if i % 2 == 0:
        return collectEvenInts(listOfInt) + [i]
    else:
        return collectEvenInts(listOfInt) + []
    
def countVowels(someString):
    '''
    Returns the number of vowels that exists in someString
    
    :param someString: is a str
    '''
    if len(someString) == 0:
        return 0
    
    if someString[len(someString)-1] in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
        return 1 + countVowels(someString[:len(someString)-1])
    else:
        return 0 + countVowels(someString[:len(someString)-1])
    
def reverseString(s):
    '''
    Returns a string in the reverse order of s
    
    :param s: is a str
    '''
    if len(s) == 0:
        return ""
    return s[len(s)-1] + reverseString(s[:len(s)-1])

def removeSubString(s, sub):
    '''
    Returns a string where all occurrences of sub are removed in the order it appears in the string
    
    :param s: is a str
    :param sub: is a str
    '''

    if sub not in s:
        return s
    
    if s[:len(sub)] == sub:
        return "" + removeSubString(s[len(sub):len(s)], sub)
    else:
        return s[0] + removeSubString(s[1:len(s)], sub)
