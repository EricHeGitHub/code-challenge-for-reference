'''
Count total set bits in all numbers from 1 to n
Given a positive integer n, count the total number of set bits in binary representation of all numbers from 1 to n.
00
01
10
11
'''
from math import floor

def TotalSetBits(n):
    n += 1
    binaryLen = len(bin(n - 1)[2:])
    totalSetBit = 0
    for i in range(1, binaryLen + 1):
        stride = 2 ** i
        totalSetBit += floor(n / stride) * stride / 2
        residue = n % stride
        totalSetBit += residue - stride / 2 if residue - stride / 2 > 0 else 0


    return int(totalSetBit)

if __name__ == "__main__":
    n = int(input("Please set the value of n:"))
    print("The total number of set bits from 1 to {0} is  {1}".format(n, TotalSetBits(n)))
