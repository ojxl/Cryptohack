# fermats theorem a^(p-1) = 1 mod p
#3^-1 mod 13
# prime modulus (p)
p = 13

# element to invert
g = 3

# Fermat's little theorem
d = pow(g, p-2, p)

print(d)


