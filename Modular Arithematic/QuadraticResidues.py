p = 29
ints = [14, 6, 11]

for a in range(1, p):  # loop through 1 to 28 (skip 0, it's trivial)
    a2 = pow(a, 2, p)  # compute a^2 modulo p
    if a2 in ints:     # check if this square matches a number in the list
        smaller_root = min(a, p - a)  # pick the smaller of the two roots
        print(f"Quadratic residue: {a2}, smaller root: {smaller_root}")
