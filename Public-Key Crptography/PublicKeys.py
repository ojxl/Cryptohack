number = 12
e = 65537
p = 17
q = 23
N = p * q  # modulus

# Encrypt the number using RSA: ciphertext = number^e mod N
ciph = pow(number, e, N)

# Print the encrypted result
print(ciph)  # encrypted number