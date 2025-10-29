from pwn import xor

label = b"label"   # pwntools works with bytes
result = xor(label, 13) # xor with integer applies to each byte
print("crypto{" + result.decode('latin-1') + "}")
