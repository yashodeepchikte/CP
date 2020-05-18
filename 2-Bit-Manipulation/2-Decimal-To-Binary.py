N = int(input("please enter a decimal number \n"))

binary = 0
base = 1

while N != 0:
    remainder = N%2
    binary = binary + remainder*base
    base = base*10
    N = N//2
print(binary)