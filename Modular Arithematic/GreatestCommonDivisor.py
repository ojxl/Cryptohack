# Define a function to compute the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    # Keep looping until the remainder becomes zero
    while b != 0:
        # Replace (a, b) with (b, a mod b) — Euclid's Algorithm step
        a, b = b, a % b
    # When b is zero, 'a' is the GCD
    return a

# Calculate and print the GCD of 66528 and 52920
print(gcd(66528, 52920))
