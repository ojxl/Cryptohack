p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# Compute Euler's Totient: (N) = (p - 1) * (q - 1)
pn = (p - 1) * (q - 1)

# Compute the private key exponent d (modular inverse of e mod (N))
d = pow(e, -1, pn)

# Print the private key exponent d
print(d)  # private key exponent