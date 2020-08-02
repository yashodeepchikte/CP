"""
Selection Sort
consider sub arrays find the min element and place it at the start 
"""

def selectionSort(A):
    n = len(A)
    for i in range(n):
        subarray = A[i:]
        min = A[i]
        min_index = i
        for j in range(i, n):
            if A[j] < min:
                min = A[j]
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    print(A)
    return A

selectionSort([9, 8,7,6,5,4,3,2,1])