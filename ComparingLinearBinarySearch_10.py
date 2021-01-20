# File: ComparingLinearBinarySearch.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 11/3/2020
# Date Last Modified: 11/6/2020
# Description of Program: This program compares the performance of linear and binary search

import random
import math

def linearSearch( lst, key ):

    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

def binarySearch( lst2, key ):

    count = 0
    low = 0
    high = len(lst2) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst2[mid]:
            high = mid - 1
        elif key == lst2[mid]:
            return (count)
           
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)

def main():
    lst = list(range(1000))
    random.shuffle(lst)
    print("Linear search:")
    nums = [10, 100, 1000, 10000, 100000]
     
    for i in nums:
        result = []
        for _ in range(i):
            key = random.choice(lst)
            temp = linearSearch(lst, key)
            result.append(temp)

        total = ((sum(result))/i)
        
        print(format('  Tests: ' + str(i), '<16'), end='')
        print(format('Average probes:' + format(total, '8.3f'), '<27'))
    
    print("Binary search:")
    lst2 = list(range(1000))
    binaryResult = []
    
    for i in range(20):
        key = random.choice(lst2)
        temp2 = binarySearch(lst2, key)
        binaryResult.append(temp2)
        
    
    total2 = ((sum(binaryResult))/i)
    diff = math.log(1000,2) - total2
    print("  Average number of probes:", format(total2, "8.3f"))
    print("  Differs from log2(1000) by:", diff)
        
main()