# import the xor helper from pwntools which XORs byte strings together
from pwn import xor

# convert the first hex-encoded key into raw bytes
key1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')

# convert the second/third combined hex-encoded key into raw bytes
key2_3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')

# convert the hex-encoded ciphertext (or data) into raw bytes
flag = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

# XOR the three byte-strings together (pwntools' xor accepts multiple arguments)
# the result is the byte-wise XOR: key1 ^ key2_3 ^ flag
print(xor(key1, key2_3, flag))
