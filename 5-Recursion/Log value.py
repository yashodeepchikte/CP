"""
this function returns the
floor value of log(n) with the givenn base
"""
def logValue(n, base):
    if n == 0:
        return -1
    if n == 1:
        return 0
    return 1 + logValue(n//2, base)

for i in range(100):
    print(i, end="---------->")
    print(logValue(i, base = 2))