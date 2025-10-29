from pwn import xor
data = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
result = xor(data, 16) # xor with integer applies to each byte
print("crypto{" + result.decode('latin-1') + "}")#i brute forced each posible byte