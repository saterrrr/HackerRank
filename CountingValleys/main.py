#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    sea_level = 0
    valleys = 0
    in_valley = False

    for step in path:
        if step == 'U':
            sea_level += 1
        else:
            sea_level -= 1

        if step == 'U' and sea_level == 0:
            in_valley = False
        elif step == 'D' and sea_level < 0 and not in_valley:
            in_valley = True
            valleys += 1

    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
