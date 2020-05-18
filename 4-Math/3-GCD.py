A = int(input("enter first number"))
B = int(input("input second number"))

(A,B) = (A,B) if A>B else (B,A)

while B:
    A, B = B, A%B
print(A)