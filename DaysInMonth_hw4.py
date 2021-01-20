
# File: DaysInMonth.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 9/23/2020
# Date Last Modified: 9/24/2020
# Description of Program: Hw 4 lets the user to input any month and year, and gives the number of days in the month

def main():
    
    month = eval(input("Enter the month: "))
    year = eval(input("Enter a year: "))
    
                 
    IsLeapYear = ( year % 4 == 0 ) and ( not ( year % 100 == 0 ) or ( year % 400 == 0 ));

    if month == 2:          # If the month is 2, then check if the year is a leap year
        if IsLeapYear:
           print ("February", year, "has 29 days")
        
        else:
           print("February", year, "has 28 days")
        
                      
    elif month == 1:                 # If the month is any other number other than 2 will print the month with the year by going through elif statements
        print ("January", year, "has 31 days")
    elif month == 3:
        print ("March", year, "has 31 days")
    elif month == 4:
        print ("April", year, "has 30 days")
    elif month == 5:
        print ("May", year, "has 31 days")
    elif month == 6:
        print ("June", year, "has 30 days")
    elif month == 7:
        print ("July", year, "has 31 days")
    elif month == 8:
        print ("August", year, "has 31 days")
    elif month == 9:
        print ("September", year, "has 30 days")
    elif month == 10:
        print ("October", year, "has 31 days")
    elif month == 11:
        print ("November", year, "has 30 days")
    elif month == 12:
        print ("December", year, "has 31 days")    
               

main()


        
