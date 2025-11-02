# Define the Extended Euclidean Algorithm to find x and y such that: a*x + b*y = gcd(a, b)
def exGcd(a, b):
	# Base case: if b is 0, gcd is a, and the coefficients are (1, 0)
	if b == 0:
		return [1, 0]

	# Recursively compute coefficients for (b, a % b)
	[x, y] = exGcd(b, a % b)

	# Compute how many times b fits into a
	n = a // b

	# Return updated coefficients: (y, x - n*y)
	return [y, x - n*y]

# Run the function with the given values and print the result
print(exGcd(26513, 32321))
