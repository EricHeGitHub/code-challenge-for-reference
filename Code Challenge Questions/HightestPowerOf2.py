'''
Given a number n, find the highest power of 2 that is smaller than or equal to n.
'''

def HighestPowerOf2(n):
    power = 0
    while n >= 2:
        power += 1
        n /= 2

    return 2 ** power

n = 19
print(HighestPowerOf2(n))
