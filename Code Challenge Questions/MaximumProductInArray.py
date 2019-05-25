'''
Given an array with both +ive and -ive integers,
return a pair with highest product.
'''

def MaximumProductInArray(arr):
    positiveMax = max(arr)
    arr.remove(positiveMax)
    positoveSecondMax = max(arr)
    arr.remove(positoveSecondMax)
    negativeMininum = min(arr)
    arr.remove(negativeMininum)
    negativeSecondMinimum = min(arr)

    if positiveMax * positoveSecondMax < negativeMininum * negativeSecondMinimum:
        return (negativeMininum , negativeSecondMinimum)
    else:
        return (positoveSecondMax, positiveMax)

arr = [-1, -3, -4, 2, 0, -5]
print(MaximumProductInArray(arr))
