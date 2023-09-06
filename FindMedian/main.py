#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    sorted_array = sorted(arr)
    n = len(sorted_array)
    
    if n % 2 == 1:  
        middle_index = n // 2
        middle_element = sorted_array[middle_index]
    else: 
        middle_index1 = (n // 2) - 1
        middle_index2 = n // 2
        middle_element1 = sorted_array[middle_index1]
        middle_element2 = sorted_array[middle_index2]
        middle_element = (middle_element1 + middle_element2) / 2.0
    return middle_element

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
