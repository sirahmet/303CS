# File: EasterSunday.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 9/9/2020
# Date Last Modified: 9/9/2020
# Description of Program: Displays any year's Eastern date\

def main(): 
    year = input("Enter year: ")

    a = (int(year)%int(19))
    b = (int(year)//int(100))
    c = (int(year)%int(100))
    d = (b/4)
    e = (b%4)
    g = ((8*b+13)//25)
    h = ((19*a+b-d-g+15)%30)
    j = (c//4)
    k = ((c%4))
    m = ((a+11*h)//319)
    r = ((2*e+2*j-k-h+m+32)%7)
    n = ((h-m+r+90)//25)
    p = ((h-m+r+n+19)%32)

    print("In " + year + " Easter Sunday is on month " + str(int(n)) + " and day " + str(int(p)) )
    
main()
