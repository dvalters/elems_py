# test strings.py
from strings import is_palindrome, is_palindrome_fast

def test_palindrome():
    """
    Test if a string is a palindrome
    """
    # Set up
    palindrome = "radar"
    not_palindrome = "magnets"

    # Act
    assert is_palindrome(palindrome) is True
    assert is_palindrome(not_palindrome) is False


def test_palindrome_fast():
    """
    Test if a string is a palindrome
    """
    # Set up
    palindrome = "radar"
    not_palindrome = "magnets"

    # Act
    assert is_palindrome_fast(palindrome) is True
    assert is_palindrome_fast(not_palindrome) is False
