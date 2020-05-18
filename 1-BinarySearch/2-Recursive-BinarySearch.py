# Recursive Binary Search algorithm

A = input("enter the array elements seperated bby a space do not use [] -- \n")
key = float(input("Enter the value of the key \n"))

A = list(map(float, A.split()))
A.sort()

low = 0
high = len(A)-1
index = -1

def BinarySearch(A, low, high, key):
    mid = int((low+high)/2)
    if (low>high):
        return -1
    if A[mid] == key:
        return mid
    elif A[mid] < key:
        low = mid + 1
        return BinarySearch(A, low, high, key)
    elif A[mid] > key:
        high = mid - 1
        return BinarySearch(A, low, high, key)
    
    
index = BinarySearch(A, low, high, key)

if index != -1:
    print("The element was found at index " + str(index))
else:
    print("The element was not found in the array")