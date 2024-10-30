"""
A series of string manipluation programs
"""

def is_palindrome(input_string: str) -> bool:
    """
    Test if string is palindrom or not
    """
    reversed_string = input_string[::-1]
    return reversed_string == input_string

def is_palindrome_fast(input_string: str) -> bool:
    """
    Faster implemnetation that does not reverse the entire string
    """
    return all(input_string[i] == input_string[~i] for i in range(len(input_string)))
