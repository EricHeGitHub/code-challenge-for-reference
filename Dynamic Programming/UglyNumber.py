'''
Question Description

Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15,
… shows the first 11 ugly numbers. By convention, 1 is included.
Given a number n, the task is to find n’th Ugly number.
'''

#U[n] represents the nth Ugly number
#U[0] = 1

n = int(input("Please input the number to calculate the ugly number:"))

U = [0] * int(n)
U[0] = 1

nextByTime2 = U[0] * 2
nextByTime3 = U[0] * 3
nextByTime5 = U[0] * 5

pointer2 = pointer3 = pointer5 = 0

for i in range(1, int(n)):
    U[i] = min(nextByTime2, nextByTime3, nextByTime5)
    if U[i] == nextByTime2:
        pointer2 += 1
        nextByTime2 = U[pointer2] * 2
    if U[i] == nextByTime3:
        pointer3 += 1
        nextByTime3 = U[pointer3] * 3
    if U[i] == nextByTime5:
        pointer5 += 1
        nextByTime5 = U[pointer5] * 5

print("The {0}th ugly number is {1}".format(n, str(U[n - 1])))
