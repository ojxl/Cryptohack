number = 12
e = 65537
p = 17
q = 23
N = p * q  # modulus

ciph = pow(number,e,N)
print(ciph)  # encrypted number