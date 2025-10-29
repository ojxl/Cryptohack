# hex_to_base64.py
import base64

# The given hex string
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 1: Decode hex string to bytes
raw_bytes = bytes.fromhex(hex_string)

# Step 2: Encode bytes into Base64
b64_encoded = base64.b64encode(raw_bytes)

# Step 3: Convert bytes → string for printing
flag = b64_encoded.decode('utf-8')

print(flag)
