# this functon uses memoisation to get fibnachi sequence

def fibon(n, known_values={}):
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n == 2:
		return 1
	
	if n in known_values.keys():
		return known_values[n]
	else:
		known_values[n] = fibon(n-1, known_values) + fibon(n-2, known_values)
		return known_values[n]



# driver code
for i in range(15):
	print(fibon(i))