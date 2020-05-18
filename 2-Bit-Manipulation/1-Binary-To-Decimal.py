N = int(input("please enter a binary number \n"))

binary = 0
base = 1

while N != 0:
    remainder = N%10
    binary = binary + remainder*base
    base = base*2
    N = N//10
print(binary)