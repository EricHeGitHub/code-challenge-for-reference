'''
Given a integer as a input and replace all the ‘0’ with ‘5’ in the integer.
Examples:
    102 - 152
    1020 - 1525
Use of array to store all digits is not allowed.
'''
from math import floor

def ReplaceAll0With5(n):
    original = n
    if n == 0:
        return 5
    position = 1
    offset = 0

    while(n != 0):
        if n % 10 == 0:
            offset += 5 * position
        n = floor(n/10)
        position *= 10
    return original + offset

num = 1040300506070
print(num)
print(ReplaceAll0With5(num))
