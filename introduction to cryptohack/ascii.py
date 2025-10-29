# 1) the list of ASCII codes we were given
nums = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# 2) convert each integer to its ASCII character using chr()
chars = [chr(n) for n in nums]   # list comprehension: makes a list of characters

# 3) join the characters into one string
flag = ''.join(chars)

# 4) print it so we can see the result
print(flag)
