A = input("enter the array elements seperated bby a space do not use [] -- \n")
key = float(input("Enter the value of the key"))

A = list(map(float, A.split()))
A.sort()

low = 0
high = len(A)-1
index = -1

while (high >= low):
    mid = int((low+high)/2)
    
    if key == A[mid]:
        index = mid
        break
    elif key > A[mid]:
        low = mid+1
    elif key < A[mid]:
        high = mid-1

if index != -1:
    print("Element was found at index " + str(index))
else:
    print("Element not found in the array")