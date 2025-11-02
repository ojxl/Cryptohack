# Elliptic curve is defined over a finite field F_p
p = 9739  # prime modulus for the finite field

# Given point P on the elliptic curve
Px = 8045  # x-coordinate of P
Py = 6936  # y-coordinate of P

# The inverse of P on an elliptic curve is the point Q = (x, -y mod p)
# Adding P + Q should give the identity element (point at infinity)
Qx = Px  # x-coordinate stays the same
Qy = (-Py) % p  # y-coordinate is negated modulo the prime p

# Print the inverse point Q
print("crypto =", {Qx, Qy})  # Expected output: Q = (8045, 1803)
