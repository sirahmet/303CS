# File: MinMax.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 9/27/2020
# Date Last Modified: 10/2/2020
# Description of Program: Hw 5 gives out the min and max value of any input integers





#At first min and max values are equal to none
min_value = None
max_value = None 
while (True):
    value = input("Enter an integer or 'stop' to end: ")
    
    
    if value == "stop":
        if min_value == None:
            print("You didn’t enter any numbers")
            break
        else:
            print("The maximum is", max_value)
            print("The minimum is", min_value)
            break
   
   
#Whenever any integer is added, make the integer equal to min and max    
    if min_value == None:
        min_value = int(value)
        max_value = int(value)
#Compare the first integer value with the second integer, and find out which is min and max
    elif int(value) > max_value:
        max_value = int(value)
    elif int(value) < min_value:
        min_value = int(value)
   
        







