# minimum swaps required to sort array containing only first n natural numbers
"""
For each index in arr[].
Check if the current element is in it’s right position or not. 
Since the array contains distinct elements from 0 to N-1, 
we can simply compare the element with it’s index in array to check if it is at its right position.
If current element is not at it’s right position then,
 swap the element with the element which has occupied its place.
Else check for next index.
"""
def swap(A, ind1, ind2):
    temp = A[ind1]
    A[ind1] = A[ind2]
    A[ind2] = temp
    return A
def sort_with_swap(A):
    swaps = 0
    for i in range(len(A)):
        while A[i] != i:
            print("swaping ", i, " ", A[i])
            A = swap(A, i, A[i])
            swaps += 1
            print(A)
        print("<---------",i ,"index was set------------>")
sort_with_swap([7, 1, 3, 2, 4, 6, 5, 0])