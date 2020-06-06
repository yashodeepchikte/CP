"""
this function returns a ^ n
"""
def exponent(a, n):
    if n == 1:
        return a
    if n == 0:
        return 1
    
    if n%2 == 0:
        return exponent(a*a, n/2)
    else:
        return a*exponent(a*a, (n)//2)
    
for i in range(10):
    print( "2 ^ ",i,"--------------->", exponent(2, i))