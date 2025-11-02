# importing helpful number conversion functions
from Crypto.Util.number import *

flag = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
#converting the large integer into its byte (text) representation
message = long_to_bytes(flag)
print(message.decode())