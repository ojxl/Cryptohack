#reference: https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.factorint
from sympy import factorint
N = 510143758735509025530880200653196460532653147

#factoring number 
factors = factorint(N)
p, q = factors.keys()

#printing 
print(min(p, q))  # smaller prime factor
