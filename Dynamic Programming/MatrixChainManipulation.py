from sys import maxsize

def MatrixChainManipulationRecursion(p, i, j): # the solution for combining ith matrix in jth matrix inclusive
    if i == j:
        return 0

    cost = maxsize

    for k in range(i, j):
        c = MatrixChainManipulationRecursion(p, i, k) \
            + MatrixChainManipulationRecursion(p, k + 1, j) \
            + p[i - 1] * p[k] * p[j]
        if c < cost:
            cost = c

    return cost

def MatrixChainManipulationDP(p, n):
    m = [[0 for _ in range(n)] for _ in range(n)] # the solution for combining ith matrix in jth matrix inclusive

    for i in range(n):
        m[i][i] = 0

    # The following solution works as it uses buttom up method: the solution order is 12, 23, 13 using the given exaple at the buttom of the script
    for L in range(2, n): # for all possible length of sub expressions
        for i in range(1, n - L + 1): # move i is the start of the exression while j is the end of the expression, the distance between i and j is always L
            j = i + L - 1
            m[i][j] = maxsize
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost

    # The following solution does not work as it does not follow buttom-up: the solution order is 12, 13, 23
    # This causes problem as solution 13 requires results of 12 and 13, when solving 13, the solution for 23 is not ready yet.
    # Therefore this solution misses out some of the counts for the operations.
    # for j in range(2, n):
    #     for i in range(1, j):
    #         m[i][j] = maxsize
    #         for k in range(i, j):
    #             cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
    #             if cost < m[i][j]:
    #                 m[i][j] = cost

    return m[1][n - 1]

if __name__ == "__main__":
    p = [10, 20, 30, 40]

    recursionResult = MatrixChainManipulationRecursion(p, 1, len(p) - 1)

    DPResult = MatrixChainManipulationDP(p, len(p))

    print("The recursion result for matrix chain manipulation is {0}.".format(recursionResult))

    print("The DP result for matrix chain manipulation is {0}.".format(DPResult))
