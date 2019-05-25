'''
Given a binary string, count number of substrings
that start and end with 1.
For example, if the input string is “00100101”,
then there are three substrings “1001”, “100101” and “101”.
'''

def SubStringStartEndWith1(s):
    n = list(s).count("1")
    return int((n - 1 + 1) * (n - 1) / 2)


s = "00100101"
print(SubStringStartEndWith1(s))
