from heapq import merge
import sys

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    lowArr = mergeSort(arr[:mid])
    highArr = mergeSort(arr[mid:])

    mergedArr = []
    low, high = 0, 0
    while low < len(lowArr) and high < len(highArr):
        if lowArr[low] < highArr[high]:
            mergedArr.append(lowArr[low])
            low += 1
        else:
            mergedArr.append(highArr[high])
            high += 1
    mergedArr += lowArr[low:]
    mergedArr += highArr[high:]
    return mergedArr

def quickSort(arr):
    if len(arr) < 2:
        return arr
    pivot = len(arr) // 2
    lowArr, pivotArr, highArr = [], [], []
    for val in arr:
        if val < arr[pivot]:
            lowArr.append(val)
        elif val > arr[pivot]:
            highArr.append(val)
        else:
            pivotArr.append(val)
    return quickSort(lowArr) + quickSort(pivotArr) + quickSort(highArr)

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

# print(mergeSort(arr))
result = quickSort(arr)
for val in result:
    print(val)