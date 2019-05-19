'''
Given a “2 x n” board and tiles of size “2 x 1”,
count the number of ways to tile the given board using the 2 x 1 tiles.
A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e., as 2 x 1 tile.
'''

def CountTiles(n):
    if n == 0 :
        return 0
    if n == 1:
        return 1

    countTiles = [0 for i in range(n + 1)]
    countTiles[0] = 1
    countTiles[1] = 1

    for i in range(2, n + 1):
        countTiles[i] = countTiles[i - 2] + countTiles[i - 1] # it is just a Fibonacci sequence
    return countTiles[n]

if __name__ == "__main__":
    n = int(input("Please input a number n for the tile width:"))
    print(CountTiles(n))
