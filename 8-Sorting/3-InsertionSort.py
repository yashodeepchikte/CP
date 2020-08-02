"""
Pick element arr[i] and insert it into sorted sequence arr[0…i-1]
"""

def insertElement(A, element, from_index, to_index):
    B = A[0:to_index] + [element] + A[to_index:from_index]+ A[from_index+1 : ]
    return B

def insertionSort(A):
    for i in range(len(A)):
        element = A[i]
        from_index = i
        for j in range(i):
            if A[j] >= A[i]:
                to_index = j 
                A = insertElement(A, element, from_index, to_index)
                break 
    print(A)
    return A

insertionSort([1,9,2,8,3,7,4,6,5])