def findMedian(A):
    
    def find(A, B):
        low = 0
        high = len(A) - 1
        found_index = -1
        while low <= high:
            mid = (low + high)//2
            if A[mid] == B:
                found_index = mid
                
                break
            elif A[mid] < B:
                low = mid +1
            elif A[mid] > B:
                high = mid -1
        if found_index != -1:
            return (found_index, 1) 
        if high == low:
            if A[low] < B:
                return (low+1, 0)
            else:
                return (low, 0)
        if high < low:
            return (high, 0)
        
    mn = len(A)*len(A[0])
    n = int((mn-1)/2)
    ci = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            print("i=", i, "j=", j)
            element = A[i][j]
            count = 0
            times_found = 0
            print("element is " , element)
            for row in range(len(A)):
                
                if row == i:
                    (finding, exist) = find(A[row], element)
                    count += finding
                    if exist :
                        if element in A[row][:j]:
                            print("A[row][:j]=", A[row][:j])
                            times_found += 1
                        times_found += 1
                else:
                    (finding, exist) = find(A[row], element)
                    count += finding + 1
                    if exist :
                        times_found += 1
                    
                print("After row", row, "count=", count, "times_found=", times_found)
                
            for k in range(times_found):
                print("count-i=",count-k )
                ci.append(count-k)
                if count-k == n:
                    return element 
            print("\n\n")
        ci.sort()
        print(ci)
        
            
findMedian(
        [
  [9, 10, 10, 13, 14, 15, 15, 15, 17, 17, 18],
  [1, 4, 9, 14, 16, 18, 19, 22, 26, 26, 27],
  [4, 6, 7, 10, 14, 20, 21, 23, 24, 27, 28],
])