from math import floor

def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

def mergeSort(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        if arr[0] > arr [1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    splitPoint = floor(len(arr) / 2)
    arr1 = arr[:splitPoint]
    arr2 = arr[splitPoint:]
    arr = mergeSort(arr1) + mergeSort(arr2)

    return arr

def quickSort(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    pick = floor(len(arr)/2)

    arrSmaller = []
    arrBigger =[]
    arrEqual = []

    for i in arr:
        if i > arr[pick]:
            arrBigger.append(i)
        elif i < arr[pick]:
            arrSmaller.append(i)
        else:
            arrEqual.append(i)

    return arrSmaller + arrEqual + arrBigger


arr = [1,5,3,2,7,4,3,7,8,4,5,7,8,7,4,2,1,15,7,32,1,8,3]

print("The result of bubble sort is :")
print(bubbleSort(arr), end = "\n")

print("The result of merge sort is :")
print(mergeSort(arr), end = "\n")

print("The result of quick sort is :")
print(quickSort(arr), end = "\n")
