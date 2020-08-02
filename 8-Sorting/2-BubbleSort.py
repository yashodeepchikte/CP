"""
Keep parsing over the array and if adjescent elements are in wrong order
swap them until there are no swaps 
By the ith traversal the last i elements will already be in the correct position
"""

def bubbleSort(A):
    n = len(A)
    for i in range(n):
        swaps = False
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swaps = True
        if not swaps:
            break
    print(A)
    return A

bubbleSort([1, 2, 3, 4, 5, 6, 7, 7, 8, 9])