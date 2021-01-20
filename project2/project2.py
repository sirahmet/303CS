# File: Project2.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/30/2020
# Date Last Modified: 11/2/2020
# Description of Program: Project 2 is a library of functions to deal with primes,
#                         including finding the prime factorization of arbitrary positive integers.

import math
#The function let us know if the num is prime or not
def isPrime ( num ):
    if (num < 2 or num % 2 == 0 ):
        return num == 2
    
    divisor = 3
    while (divisor <= math.sqrt(num)): 
        if (num % divisor == 0):
            return False
        else:
            divisor += 2
    return True

#This let us figure out the factors of a num
def factor (num): 
    firstPrime = 2 
    factor = []
    while num > 1:
        if num % firstPrime ==0:
            factor.append(firstPrime)
            num = num/firstPrime

        else:
            firstPrime += 1+firstPrime % 2
    return(factor)


def main():
    print("Welcome to the Prime factory!")
    print()
    while True:        
        command = input("Enter a command (factor, isprime, end): ")
        if command.lower() == "end":
            print("Thanks for using our service! Goodbye.")
            break

        if command.lower() == "factor":
            num = int(input("Enter an integer > 1: "))
            if num <= 1:
                print("Illegal input: " + str(num) + "; input must be an integer > 1." )
                print()
            else:
                print(factor(num))
                print()
                            
        elif command.lower() == "isprime":
            num = int(input("Enter an integer > 1: "))
            if num < 1:
                print("Illegal input: " + str(num) + "; input must be an integer > 1." )
                print()
            elif isPrime(num) == False:
                print("The number", num , "is not prime")
                print()
            elif isPrime(num) == True:
                print("The number", num , "is prime")
                print()                

        else:
            print("Command", command, "not recognized. Try again!")
            print()

main()

