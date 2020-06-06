"""
finding maximum value using recursion
"""

def findMax(arr, n):
    if n == 1:
        return arr[0] 
    else:
        x =  findMax(arr, n-1)
    if arr[n-1] < x:
        return x
    else:
        return arr[n-1]
    
arr = [110000,5,2,3,6,7,2,8,10,1,-9, 100]
findMax(arr, len(arr))

def findMin(arr, n=len(arr)):
    if n == 1:
        return arr[0]
    else:
        x = findMin(arr, n-1)     # this if else block will return the first element
    
    if x < arr[n-1]:
        return x
    else:
        return arr[n-1]         # this if else blockk copairs the max element with each element left to right
    
findMin(arr)