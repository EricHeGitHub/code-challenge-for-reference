'''
The problem is to count all the possible paths from top left to bottom right of
a mXn matrix with the constraints that from each cell
you can either move only to right or down
'''
def CountAllPossiblePaths(m,n):
    arr = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        arr[i][n - 1] = 1

    for i in range(n):
        arr[m - 1][i] = 1

    arr[m - 1][n - 1] = 0

    for i in range(m - 2, -1 , -1):
        for j in range(n - 2, -1, -1):
            arr[i][j] = arr[i + 1][j] + arr[i][j + 1]
    return arr[0][0]



m = 100
n = 100
print("The number of ways to travel from (0,0) to ({0},{1}) is {2}".format(m, n, str(CountAllPossiblePaths(m,n))))
