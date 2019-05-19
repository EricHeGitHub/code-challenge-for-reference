'''
Given a gold mine of n*m dimensions.
Each field in this mine contains a positive integer which is the amount of gold in tons.
Initially the miner is at first column but can be at any row.
He can move only (right,right up,right down)
that is from a given cell,
the miner can move to the cell diagonally up towards the right
or right or diagonally down towards the right.
Find out maximum amount of gold he can collect
'''

def GoldMine(mat, m, n):
    #input mat has m rows and n columns
    #maxGoldCollected[i][j] represents the maximum value of gold that can be collected at position(i, j)
    #following the action rule
    maxGoldCollected = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(m):
            if i == n - 1:
                right = 0
            else:
                right = maxGoldCollected[j][i + 1]

            if j == 0:
                rightUp = 0
            else:
                if i != n - 1:
                    rightUp = maxGoldCollected[j - 1][i + 1]
                else:
                    rightUp = 0

            if j == m - 1:
                rightDown = 0
            else:
                if i != n - 1:
                    rightDown =  maxGoldCollected[j + 1][i + 1]
                else:
                    rightDown = 0
            maxGoldCollected[j][i] = mat[j][i] + max(right, rightDown, rightUp)
    return max(maxGoldCollected[k][0] for k in range(m))

if __name__ == "__main__":
    mat1 = [[1, 3, 3],
           [2, 1, 4],
           [0, 6, 4]];
    mat2 = [[1, 3, 1, 5],
            [2, 2, 4, 1],
            [5, 0, 2, 3],
            [0, 6, 1, 2]]
    print(GoldMine(mat1, len(mat1[0]), len(mat1)))
