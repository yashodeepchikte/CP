"""
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
"""



""""

this code is not working


"""

def merge(left, right):
    result = left
    print("left for merge = ", left)
    print("right foe merge = ", right)
    print("")
    for ele in right:
        for i in range(len(result)):
            if result[i] > ele:
                result = result[0: i] + [ele] + result[i:]
                break
            if i == len(result)-1:
                result = result + [ele]
                break
    return result

count = 0
def mergeSort1(A, left, right):
    global count
    count += 1
    #print("count = ", count)
    if count > 10:
        return [0] 
    if left == right:
        return [A[left]]

    mid = int((left + right) // 2)
    
    #print(type(mid))
    print("left = ", left, "right = ", right, "mid = ", mid)
    print("A = ", A[left:right])
    left_halve = A[left: mid+1]
    right_halve = A[mid+1: right]
    
    #print(A)
    print("S = ", left_halve, end = " ")
    print(right_halve, end = "\n")
    print(" ")
        
    left_halve = mergeSort(A, left, mid+1)   
    right_halve = mergeSort(A, mid+1, right)
    
    A = merge(left_halve, right_halve)
    #print(A)
    return A

count = 0
def mergeSort(A):
    global count
    count += 1
    #print("count = ", count)
    if count > 30:
        return [0] 
    if len(A) == 1:
        print("i am returning ", A)
        return A
    left = 0
    right = len(A)
    mid = (left+right)//2
    print("A = ", A)
    print("s = ", A[:mid], " ", A[mid:], "\n")

    left_halve = mergeSort(A[:mid])
    right_halve = mergeSort(A[mid:])
    merge(left_halve, right_halve)    
    
A = [1, 121, 181, 81, 92, 11, 131, 13]
mergeSort(A)






