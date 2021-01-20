# File: RecursiveFunctions.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50705
#
# Date Created:11/18/2020
# Date Last Modified:11/20/2020
# Description of Program: 






def sumItemsInList( L ):
   # """ Given a list of numbers, return the sum. """
   if L == []:
      return 0
   else:
      return L[0] + sumItemsInList( L[1:] )



def countOccurrencesInList( key, L ):
# """ Return the number of times key occurs in 
   
   if L == []:
      return 0
   elif key == L[0]:
      return 1 + countOccurrencesInList( key, L[1:] )
   else:
      return countOccurrencesInList( key, L[1:] )


def addToN ( n ):
#Add up the non-negative integers to n.
#E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. 
   if (n <= 1):
      return n
   return n + addToN(n - 1)

def findSumOfDigits( n ):
#Return the sum of the digits in a non-negative integer. 
   if n == 0:
      return 0
   return ((n % 10) + (findSumOfDigits (int(n/10))))

def decimalToBinary( n ):
#    """ Given a nonnegative decimal n, return the 
#    binary representation as a string. """
   if n == 0: 
      return 0
   else: 
      return (n % 2 + 10 * decimalToBinary(int(n // 2))) 

def decimalToList( n ):
#    """ Given a positive decimal integer, return a list of the 
#    digits (as strings). """
      if n == 0:
         return []

      else:
         return [str(n % 10)] + decimalToList(n // 10)


def isPalindrome( s ):
#    """ Return True if string s is a palindrome and False
#    otherwise. Count the empty string as a palindrome. """

   if len(s) <2: 
      return True
   if s[0] != s[-1]: 
      return False
   return isPalindrome(s[1:-1])      
   


def findFirstUppercase( s ):
#    """ Return the first uppercase letter in 
#    string s, if any.  Return None if there
#    is none. """
    if s == "":
        return None
    elif s[0].isupper():
        return s[0]
    else:
        return findFirstUppercase(s[1:])


def findFirstUppercaseIndexHelper( s, index ):
#    """ Helper function for findFirstUppercaseIndex. """
   if len(s) <= index:
      return -1

   if (s[index].isupper()): 
      return index
   else:
      return findFirstUppercaseIndexHelper(s, index+1)


# # The following function is already completed for you.  But 
# # make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
#    """ Return the index of the first uppercase letter in 
#    string s, if any.  Return -1 if there is none.  This one 
#    requires a helper function, which is the recursive 
#    function. """
   return findFirstUppercaseIndexHelper( s, 0 )
