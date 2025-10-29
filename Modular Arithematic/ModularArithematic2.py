# Small examples with p = 17 just gonna text it first
p = 17

#pow is built in modular exponentiation
print(pow(3, 17, p))  # 3^17 mod 17
print(pow(5, 17, p))  # 5^17 mod 17
print(pow(7, 16, p))  # 7^16 mod 17 (Fermat's theorem)

# Big example with p = 65537
p = 65537
base = 273246787654
exp = 65536
print(pow(base, exp, p))  # 273246787654^65536 mod 65537
