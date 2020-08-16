

# this function will return all the permutations of a string using recursion

def permutations_of_string(s):

	if len(s) == 1:
		return s

	output = []

	for i in range(len(s)):
		for perm in permutations_of_string(s[:i]+s[i+1:]):
			output += [s[i] + perm]
	return output
