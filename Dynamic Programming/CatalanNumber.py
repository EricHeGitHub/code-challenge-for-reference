'''
Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.
1) Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3,
    possible expressions are ((())), ()(()), ()()(), (())(), (()()).

2) Count the number of possible Binary Search Trees with n keys

3) Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.

The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
'''

def CatalanNumber(n):
    catalanArr = [0] *  (n + 1)
    _CatlanNumber(n, catalanArr)
    return catalanArr

def _CatlanNumber(n, catalanArr):
        if n == 0:
            catalanArr[0] = 1
            return catalanArr[0]
        elif n == 1:
            catalanArr[1] = 1
            return catalanArr[1]
        else:
            if catalanArr[n] != 0:
                return catalanArr[n]
            else:
                for i in range(n):
                    catalanArr[n] += _CatlanNumber(i, catalanArr) * _CatlanNumber(n - 1 - i, catalanArr)
                return catalanArr[n]


if __name__ == "__main__":
    n = int(input("Please input a number n for Catalan:"))
    catalanArr = CatalanNumber(n)
    for i in catalanArr:
        print(i, end = " ")
    print()
