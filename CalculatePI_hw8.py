# File: CalculatePI.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50695
# 
# Date Created: 10/20/2020
# Date Last Modified: 10/23/2020
# Description of Program: It is a program that finds a new pi. As num increases the new pi increases


import math
import random

def computePI ( numThrows ):
    x = 0
    
    for _ in range(numThrows):
        xPos = random.uniform (-1.0, 1.0)
        yPos = random.uniform (-1.0, 1.0)

        if math.hypot(xPos, yPos)>=1:
          x +=1
        
        newPi = float(4*(float(numThrows)-x)/numThrows)

    return newPi


def main():
    nums = [100, 1000, 10000, 100000, 1000000, 10000000]
    for i in nums:
        newPi = computePI(i)

        diff = float(format(newPi - math.pi, '8.6f'))
        #if diff is positive, then add a plus sign
        if diff > 0:
            diff = '+' + str(diff)

        print(format('num = ' + str(i), '<17'), end='')
        print(format('Calculated PI = ' + format(newPi, '8.6f'), '<27'), end='')
        print(format('Difference = ' + str(diff), '<22'))


main()

