'''
Given a set of n elements, find number of ways of partitioning it.

Input:  n = 2
Output: Number of ways = 2
Explanation: Let the set be {1, 2}
            { {1}, {2} }
            { {1, 2} }

Input:  n = 3
Output: Number of ways = 5
Explanation: Let the set be {1, 2, 3}
             { {1}, {2}, {3} }
             { {1}, {2, 3} }
             { {2}, {1, 3} }
             { {3}, {1, 2} }
             { {1, 2, 3} }.
'''

def PartitionNumbers(n):
    #partitionArr[n][k] is to segment n elements into k partitions
    partitionArr = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    partitionArr[0][0] = 1

    for j in range(n + 1):
        partitionArr[j][0] = 0
        partitionArr[j][1] = 1

    for k in range(1, n + 1):
        partitionArr[0][k] = 0

    for k in range(2, n + 1):
        for j in range(1, n + 1):
            partitionArr[j][k] = partitionArr[j - 1][k - 1] + k * partitionArr[j - 1][k]

    return sum(partitionArr[n][i] for i in range(n + 1) )

if __name__ == "__main__":
    n = int(input("Please input a number n for the set size:"))
    print(PartitionNumbers(n))
