'''
Given an array arr[] of integers which indicates the stock price on the market for each hour,
find out the best time to buy, to sell and the maximum profit that could be made for the day.

This question is the equivalent to:
Gien an array arr[] of integers,
find out the maximum difference between any two elements such that larger element appears after the smaller number.
'''

def StockSales(arr):
    minimalValueSeen = arr[0]
    minimalValueIndex = 0
    maxValueIndex = 1
    maxDifference = arr[1] - arr[0]

    for i in range(1, len(arr)):
        minimalValueSeen = min(arr[i], minimalValueSeen)

        if maxDifference < arr[i] - minimalValueSeen:
            maxDifference = arr[i] - minimalValueSeen
            maxValueIndex = i
            minimalValueIndex = arr.index(minimalValueSeen)

    if minimalValueIndex == maxValueIndex:
        return None, None, None
    return minimalValueIndex, maxValueIndex, maxDifference

if __name__ == "__main__":
    arr1 = [2, 3, 10, 6, 4, 8, 1]
    arr2 = [7, 9, 5, 6, 3, 2]
    arr3 = [1, 2, 90, 10, 110]
    arr4 = [80, 2, 6, 3, 100]
    arr5 = [7,6,5,4,3,2,100,1]

    arr = [arr1, arr2, arr3, arr4, arr5]

    for i in arr:
        bestBuyTime, bestSellTime, largestProfit = StockSales(i)
        if largestProfit is None:
            print("No solution found.")
        else:
            print("The best time to buy the stock is {0}, the best time to sell the stock is {1} and the max profit is {2}".format(bestBuyTime, bestSellTime, largestProfit))
