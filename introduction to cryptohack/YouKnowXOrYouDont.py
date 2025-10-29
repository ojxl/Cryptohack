from itertools import cycle

ct_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
ct = bytes.fromhex(ct_hex)

# Known crib
crib = b"crypto{"

# derive first 7 key bytes
derived = bytes(ct[i] ^ crib[i] for i in range(len(crib)))
print("derived key fragment:", derived, derived.decode('ascii', errors='replace'))

# guess full key (readable English guess)
key = b"myXORkey"

# decrypt by repeating key
pt = bytes(c ^ k for c, k in zip(ct, cycle(key)))
print(pt.decode())
