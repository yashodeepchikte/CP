"""
multiplying two numbers recursively
"""
def multiply(a, b):
    if b == 0:
        return 0
    if b%2 == 0:
        return multiply( a+a, b//2 )
    return multiply( a+a, b//2 ) + a

for i in range(10):
    for j in range(10):
        print( i , "X", j, " = ", multiply(i, j))
    print("<--------------------->")