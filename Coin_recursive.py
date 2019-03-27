#problem:
#You are working at the cash counter at a fun-fair, and you have different types of coins available to you 
#in infinite quantities. The value of each coin is already given. 
#Can you determine the number of ways of making change for a particular number of units using the given types of coins?

#Coin Problem using recursive solution

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getWays function below.
def getWays(n, c):
    return _getWays(n, c, len(c))

def _getWays(n, c, m):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0 and n >= 1:
        return 0
    return _getWays(n, c, m - 1) + _getWays(n - c[m - 1], c, m)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    fptr.write(str(ways) + '\n')
    fptr.close()
