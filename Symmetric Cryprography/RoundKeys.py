state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

#got this after i ran initial add_round_key function
matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 114],
    [48, 117, 110, 100],
    [107, 51, 121, 125]
]


def add_round_key(s, k):
    # XOR each element in the matrix
    return [[s[row][col] ^ k[row][col] for col in range(4)] for row in range(4)]

#same function from the other file StructureOfAES.py
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    #We take the rows and join them back together into one sequence.
    return bytes([matrix[row][col] for row in range(4) for col in range(4)])


print(add_round_key(state, round_key))

print(matrix2bytes(matrix).decode())
