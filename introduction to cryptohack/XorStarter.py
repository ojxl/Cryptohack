from pwn import xor

label = b"label"   # pwntools works with bytes
result = xor(label, 13) # xor with integer applies to each byte
#'latin-1' is the name of a text encoding, also known as ISO-8859-1.
# It is a character encoding where every byte value (0–255) maps directly to the same Unicode code point
#https://docs.python.org/3/library/codecs.html#encodings-and-unicode
print("crypto{" + result.decode('latin-1') + "}")
