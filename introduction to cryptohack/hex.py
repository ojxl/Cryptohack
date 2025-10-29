# hex_decode.py
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# convert hex to bytes
b = bytes.fromhex(hex_string)

# decode bytes to text (UTF-8)
flag = b.decode('utf-8')

print(flag)
