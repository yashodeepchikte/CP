N = int(input("please enter a positivee number \n"))



def root(A):
    low = 0
    high = A
    val = 0
    while low<=high:
        mid = (high + low)//2
        if mid*mid == A:
            return mid
        if mid*mid < A:
            val = mid
            low+=1
        else:
            high-=1
    return val

        
print(root(N))