# File: ProblemsFromExam1.py
# Student: Ahmet Nalcaci 
# UT EID: An27394
# Course Name: CS303E
# Unique Number: 50695
# 
# Date Created: 10/12/2020
# Date Last Modified: 10/16/2020
# Description of Program: Hw#7 is Multiple exam problems

# Assignment:
# Take this file and modify it at the locations marked
#  < your code goes here >
# to solve each of the 7 problems.  If you need to import
# any modules, import them.  These are the problems
# from Exam1 (version 1), with some slight variations.  

# Submit it on Canvas by Friday 10/16 at midnight. 
# 
# Be sure to fill in the header information at the top. 

#----------------------------------------------------------------------\

# 1. Write the body of the following function that accepts as parameters
# the radius and length of a cylinder and computes and prints the area
# and volume of the cylinder using the following formulas:
# 
# area = radius * radius * pi
# 
# volume = area * length
# 
# Print two decimal places after the decimal point. Remember that pi is
# defined in the math module.  PRINT, do not return your answer.
# 
# For example, a call to computeAreaVolumeForCylinder( 5.5, 12 ) would print:
# The area is 95.03
# The volume is 1140.40

def computeAreaVolumeForCylinder( r, l ):
    import math
    #r = (float(input("Enter radius: ")))
    #lenght = (float(input("Enter length: ")))
              
    area = r * r * math.pi
 
    volume = area * l
    
    print("The area is", (format(area,".2f")))
    print("The volume is", (format(volume,".2f")))



    
### ----------------------------------------------------------------------
##
### 2. Fill in the following function to take a lower case letter and return
### that letter in upper case. If the input is not a lower case letter,
### simply return the input character. You may assume that the input is a
### single character. The ASCII codes for upper case 'A' to 'Z' are 65 to
### 90, and the ASCII codes for lower case 'a' to 'z' are 97 to 122. You
### may not use any string methods except ord() and chr(). Do NOT use
### .upper(), .lower(), .islower(), etc.
### 
### For example, if the input is 'q' you should return 'Q'.  Any of 'a',
### '9', '%' should be returned unchanged.
### 
### Return your answer, do NOT print it.
## 
def myUpper( ch ):
   
    
    if (ord(ch) > 64) and (ord(ch) < 91):
        return(ch)
        
    elif (ord(ch) > 96) and (ord(ch) < 123):
        x = ord(ch) - 32
        return(chr(x))
    else:
        return ch
    



### ----------------------------------------------------------------------
##
### 3. Complete the function below that sums the following series:
### 
###      (1 * 2) + (2 * 3) + (3 * 4) + ... + (n-1 * n)
### 
### Your function should use a for loop to compute the answer. Return,
### don't print, the answer.  You can assume that n is a positive integer
### greater than 1.  For example if n is 4, this is the series (1 * 2) +
### (2 * 3) + (3 * 4) and your function should return 20.
##
def sumSeries( n ):

    z = 0
    for i in range(n):
        
        x = (i * (i+1)) 
        z = x+z

        
        return(z)





### ----------------------------------------------------------------------
##
### 4. Complete the following program that takes as parameter a
### nonnegative integer n and prints n even integers starting with 2.  You
### can assume the input is a nonnegative integer, but don't assume it's
### nonzero. There should be 8 even integers per line, and the numbers
### should be separated by one space.  Print a newline at the end.  For
### example: printEvens( 13 ) will print the following pattern:
### 2 4 6 8 10 12 14 16 
### 18 20 22 24 26
### and printEvens( 0 ) will just print a newline.
##
def printEvens( n ):
    if n == 0:
        print()

    for i in range (1, n+1):
        while i % 9 == 0:           
            print()
            print (2*i , end = " ")
            break
      
        else:
            
            print (2*i , end = " ")

    
    

### ----------------------------------------------------------------------
##
##
### 5. Fill in the body of the following function that takes in three
### integer parameters and displays them in non-decreasing order. You can
### assume that the numbers entered are integers. Do NOT use lists, min(),
### max(), or the sort utility.  The point is to use if tests.
### 
### sortThreeIntegers( 39, 2, 5 ) should display:
### The numbers in order are: 2 5 39
### 
### sortThreeIntegers( 14, -12, -1000 ) should display:
### The numbers in order are: -1000 -12 14
##
def sortThreeIntegers( x, y, z ):
    
    if (x > y) and (x>z):
        if (y>z):
            print("The numbers in order are:", z,y,x)
        else:
            print("The numbers in order are:", y,z,x)

    if (y>x) and (y>z):
        if (x>z):
            print("The numbers in order are:", z, x, y)
        else:
            print("The numbers in order are:", x,z,y)

    if (z>y) and (z>x):
        if (y>x):
            print("The numbers in order are:", x,y,z)
        else:
            print("The numbers in order are:", y,x,z)




##----------------------------------------------------------------------
##
### 6. Fill in the following function that prints out the total of a
### series of positive floating-point (FP) numbers entered by the user.  The
### user should be prompted with the message "Enter a floating-point
### number >= 0:".  You do not need to check that the input is a
### FP number. If the user correctly enters a positive FP number, handle
### it and prompt the user for the next number with the same message.  If
### the user enters a negative number, your program should print 
### "Number must be >= 0.  Try again:" and wait for another number.
### Negative numbers should not be added to the total.  If the user enters
### a zero, that is an indication that the user is finished entering
### numbers.  You program should print out "The sum of the numbers is:"
### followed by the total.  You do not need to round the total. 
### Below are two runs of the program:
### 
### Enter a floating-point number >= 0: 3.5
### Enter a floating-point number >= 0: 2
### Enter a floating-point number >= 0: -17.9
### Number must be >= 0. Try again: 23
### Enter a floating-point number >= 0: 5
### Enter a floating-point number >= 0: 0
### The sum of the numbers is:  33.5
### 
### Enter a floating-point number >= 0: 0
### The sum of the numbers is:  0

def sumPositiveFPNumbers():
    num = None
    total = 0

    while (num != 0):
        num = float(input("Enter a floating-point number >= 0: "))

        # validation loop
        while (num < 0):
            num = float(input("Number must be >= 0. Try again: "))
        
        total += num
    print("The sum of the numbers is:", total)
         

### ----------------------------------------------------------------------
##
### 7. Complete the following function that accepts from the user a
### three-digit integer (i.e, in the range 100 to 999), and prints the
### reverse of that integer.  You can assume that the input is an integer, but
### should not assume it's in the right range.  If it's not in the right
### range, print "Illegal input:" and the number.  Here are three sample runs:
### 
### Enter a three digit decimal integer: 123
### The number in reverse is: 321
### 
### Enter a three digit decimal integer: 1234
### Illegal input: 1234
### 
### Enter a three digit decimal integer: 333
### The number in reverse is: 333
      
def printReverse():
    x = int(input("Enter a three digit decimal integer: "))
    test_num = 0
    switch = True
    
    if (99 > x) or (x > 999):
        print("Illegal input:", x)
        switch = False

    if switch:  
        while(x>0):
            remainder = x % 10
            test_num = (test_num * 10) + remainder
            x = x // 10

        print("The number in reverse is:",test_num)
        

        

   
