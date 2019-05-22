'''
Given n friends, each one can remain single or can be paired up with some other friend.
Each friend can be paired only once.
Find out the total number of ways in which friends can remain single or can be paired up.

This is a variation of set partition problem
'''

def FriendPairing(n):
    # P(n): the number of ways for pairing n people
    P = [0 for _ in range(n + 1)]
    P[0] = 0
    P[1] = 1
    P[2] = 2 #need to go up to 2 as 2 does not follow the deriviation
    for i in range(3, n + 1):
        P[i] = P[i - 1] + (i - 1) * P[i - 2]
    return P[n]

if __name__ == "__main__":
    n = int(input("Please give the number of friends to pair:"))
    print(FriendPairing(n))
