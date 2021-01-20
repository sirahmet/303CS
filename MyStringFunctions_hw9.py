# File: MyStringFunctions.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/29/2020
# Date Last Modified: 10/30/2020
# Description of Program: Write our on functions to manipulate instances of that data type


def myAppend( str, ch ):
    # Return a new string that is like str but with 
    # character ch added at the end
    return str + ch


def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    counter = 0
    for i in str:
        if ch == i:
            counter += 1
    return counter


def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2 in order.
    return str1 + str2


def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    if len(str) <=0:
        print("Empty string: no min value")
        return None

    lowest = ord(str[0])
    for i in range(1, len(str)):
        test = ord(str[i])
        if test < lowest:
            lowest = test
    return chr(lowest)


def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if i > len(str):
        print("Invalid index")
        return None

    newStr = ''
    for j in range(len(str)):
        if i == j:
            newStr += ch
            newStr += str[j]
        else:
            newStr += str[j]
    return newStr


def myPop( str, i ):
    # Return two results: 
    # 1. a new string that is like str but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(str), and return str unchanged and None
    if i >= len(str):
        print("Invalid index")
        return (str, None)

    value = ''
    newStr = ''
    for j in range(len(str)):
        if i == j:
            value = str[j]
        else:
            newStr += str[j]
    return newStr, value


def myFind( str, ch ):
     # Return the index of the first (leftmost) occurrence of 
     # ch in str, if any.  Return -1 if ch does not occur in str.
    for i in range(len(str)):
        if ch == str[i]:           
            return i
    return -1


def myRFind( str, ch ):
     # Return the index of the last (rightmost) occurrence of 
     # ch in str, if any.  Return -1 if ch does not occur in str.
    for i in range(len(str)-1, -1, -1):
        if ch == str[i]:
            return i
    return -1


def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch  
    # removed.  If there is none, return str.
    if ch not in str:
        return str

    newStr = str[:]
    index = 0                   
    for i in range(len(str)):                 
        if ch == str[i]:
            index = i 
            break
    return myPop(newStr, index)[0]


def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    newStr = ''
    for i in range(len(str)):                 
        if ch == str[i]:
            continue
        else:
            newStr += str[i]
    return newStr


def myReverse( str ):
     # Return a new string like str but with the characters
     # in the reverse order. 
    result = ''
    for i in range(len(str)-1,-1,-1):
        result += str[i]
    return result
