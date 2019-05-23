'''
Number of subsequences of the form a^i b^j c^k
Given a string, count number of subsequences of the form aibjck,
i.e., it consists of i ’a’ characters,
followed by j ’b’ characters,
followed by k ’c’ characters
where i >= 1, j >=1 and k >= 1.

This question is like DP problem but does not require tabulation or memorization.
'''

def countSubsequences(s):
    aCount = 0
    bCount = 0
    cCount = 0

    for i in s:
        if i == "a":
            '''
            1: a start a new subsequence
            aCount: a is part of existing subsequence
            aCount: a is not part of existing subsequence
            '''
            aCount = 1 + aCount + aCount
        if i == "b":
            '''
            aCount: b start a new subsequence following a sequences of 'a'
            bCount: b is part of existing subsequence
            bCount: b is not part of existing subsequence
            '''
            bCount = aCount + bCount + bCount

        if i == "c":
            '''
            bCount: c start a new subsequence following a sequences of 'a' and 'b'
            aCount: c is part of existing subsequence
            aCount: c is not part of existing subsequence
            '''
            cCount = bCount + cCount + cCount
    return cCount

if __name__ == "__main__":
    s = input("Please set a string consisting of a, b and c:")
    print("The total number of subsequence in form of aj, bj and cj is {0}".format(countSubsequences(s)))
