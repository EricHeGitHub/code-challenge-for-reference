'''
Question Description:

The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation

Given a number n, print n-th Fibonacci Number.
'''

def Fibonacci(n):
    F = [-1] * (n + 1)
    return _Fibonacci(n, F)

def _Fibonacci(n, F):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if F[n] != -1:
        return F[n]
    F[n] = _Fibonacci(n - 1, F) + _Fibonacci(n - 2, F)
    return F[n]

if __name__  == "__main__":
    n = int(input("Please input a number n:"))
    print("The {0}th Fibonacci number is {1}".format(n,Fibonacci(n)))
