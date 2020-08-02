"""
Keep parsing over the array and if adjescent elements are in wrong order
swap them until there are no swaps 

1. Base condition =  if len(A) == 1 return
2. The first traversal will set the last element
3. recur with array for all but the last element
"""

def recursiveBubbleSort(A):
    n =  len(A)
    if n == 1:
        return A
    swaps = False
    for j in range(n-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            swaps = True
    if swaps == False:
        return A
    A = recursiveBubbleSort(A[:-1]) + [A[-1]]
    return A

recursiveBubbleSort([1,3,2,5,2, 3,1,123,123,432,1312414,123,213,1433,124,14,14,1,41,43,523,412,4,23524,4,25,5,6])