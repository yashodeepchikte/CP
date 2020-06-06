"""
McCarthy 91
this function returns 91 for any input less than 101 without using 91 anywhere
"""

def mech91(n):
    if  n > 100:
        return n - 10
    else:
        return mech91(mech91(n+11))
    
for i in range(80, 110):
    print(i, "------------------->", mech91(i))