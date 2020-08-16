# Given an array of distinct integers from 0 to len(array) 
# find how many Swaps are required to sort the array

def sort_arr(arr):
    swaps = 0
    running = True
    arr = list(map(lambda x: x-1, arr))

    while running:
        swapped = False
        # we need arr[i] == i
        # if not set arr[arr[i]] = arr[i] and arr[i] = arr[arr[i]]
        for i in range(len(arr)):
            
            
            if arr[i] == i:
                pass
            else:

            
                temp1 = arr[i]
                temp2 = arr[arr[i]]
        
                arr[arr[i]] = temp1
                arr[i] = temp2
    
                
                swapped = True
                swaps += 1
          

        if  not swapped:
            running = False
            break
    
    print("Array = ", arr)
    print("Swaps required = ", swaps)
    
sort_arr([2, 3, 4, 1, 5])
