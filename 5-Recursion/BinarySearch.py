"""
Binary search using recursion
"""

def binarySearch(arr, n, left, right):
    print("Left ----------->", left)
    print("Right----------->", right)
    
    mid = (left + right )//2
    if left > right:
        return -1
    elif arr[mid] == n:
        return mid
    elif arr[mid] < n :
        left = mid + 1
        return binarySearch(arr, n, left, right)
    elif arr[mid] > n :
        right = mid - 1
        return binarySearch(arr, n, left, right)
arr = [0,1,2,3,4,5,6,7,8,9]

for i in range(10):
    print("index of ", i, "-------------->", binarySearch(arr, i, 0, len(arr)-1))
    print("-----------------------------------------------------------------------------")