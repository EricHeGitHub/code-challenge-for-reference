'''
Given an array of integers,
replace every element with the next greatest element
(greatest element on the right side) in the array.
Since there is no element next to the last element, replace it with -1.
For example, if the array is {16, 17, 4, 3, 5, 2},
then it should be modified to {17, 5, 5, 5, 2, -1}.
'''

def ReplaceElement(arr):
    maxRightValue = arr[-1]
    arr[-1] = -1

    for i in range(len(arr) - 2, -1, -1):
        temp = arr[i]
        arr[i] = maxRightValue
        if maxRightValue < temp:
            maxRightValue = temp
    return arr


arr = [16, 17, 4, 3, 5, 2]

print(ReplaceElement(arr))
