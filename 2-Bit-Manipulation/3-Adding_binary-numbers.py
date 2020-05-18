A = input("Enter first binary number")
B = input("Enter second binary number")
A_bin = int(A)
B_bin = int(B)
if len(A) != len(B):
    if len(A) > len(B):
        comp = len(A) - len(B)
        B = "0"*comp + B
    else:
        comp = len(B) - len(A)
        A = "0"*comp + A

A = [0] + list(map(int, list(A)))
B = [0] + list(map(int, list(B)))
Carry = [0 for i in range(len(A))]
result =[0 for i in range(len(A))] 

def binaryToDec(N):
    binary = 0
    base = 1
    
    while N != 0:
        remainder = N%10
        binary = binary + remainder*base
        base = base*2
        N = N//10
    return binary

A_dec = binaryToDec(A_bin)
B_dec = binaryToDec(B_bin)


for i in range(len(A)-1, -1, -1):
    
    if A[i] + B[i] + Carry[i] == 0: 
        res = 0 
        carry = 0
    elif A[i] + B[i] + Carry[i] == 1:
        res = 1
        carry = 0
    elif A[i] + B[i] + Carry[i] == 2:
        res = 0
        carry = 1
    elif A[i] + B[i] + Carry[i] == 3:
        res = 1
        carry =1
        
    result[i] = res
    
    if i < len(A):
        Carry[i-1] = carry        

print(str(A) + "---------->" + str(A_dec))
print(str(B) + "---------->" + str(B_dec))

print("---------------------------------------------------------------")
print(str(Carry) +  "----------> Carry"  )
print("-----------------------------------------")
print(str(result)+ "----------> Result")

result = list(map(str, result))
result_dec = binaryToDec(int("".join(result)))
print("result="+ "".join(result) + "-------------->" + str(result_dec))