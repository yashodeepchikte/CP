def getBinary(n):
#    print("n = ",  n)
    if n==1:
        print(1, end=" ")
        return 
    if n == 0:
        print(0, end = " ")
        return
    getBinary(n//2)
    print(n%2, end=" ")
        
for i in range(10):
    print(i, end = "------> ")
    getBinary(i)
    print(" ")
getBinary(10)