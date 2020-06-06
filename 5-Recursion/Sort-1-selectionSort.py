"""
this function performs selection sort
"""
def findMinIndex(arr, start):
    print("array inside findmin =======> ", arr)
    if len(arr)==0:
        return
    minValue = 100**100
    minIndex = 0
    for i in range(start, len(arr)):
        if arr[i] < minValue:
            minValue = arr[i]
            minIndex = i
    return minIndex

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = findMinIndex(arr, i)
        print("Arr =======> " , arr)
        print("min index =======> ", minIndex)
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
        print("ARRAY ======> ", arr)
        print("--------------------------------------------------")
    return arr

arr = [10, 9, 8, 68, 47, 26, 15, 34, 53, 72, 1]
print(selectionSort(arr))