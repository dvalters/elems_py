"""
PRIMITIVE TYPES

"""

SOME_INT = 345

def count_bits(x: int) -> int:
    """Count the number of bits that are set 
    to 1 in a non-negative integer
    """
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


def parity(x: int) -> int:
    """Determine the parity of a number"""
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

def parity_better(x: int) -> int:
    """Improvement: Erase lowest set bit for 
    reducing time complexity"""
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # Drop the lowest set bit of x
    return result




if __name__=="__main__":
    integer = 513
    binrep = bin(integer)
    result = count_bits(integer)
    print(f"The value of {integer} in binary is {binrep}")
    print(f"Number of 1 bits in {integer} is {result}")