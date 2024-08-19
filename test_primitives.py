import pytest

from primitives import count_bits, parity

@pytest.mark.parametrize("test_input, expected", [(1,1), (2,1), (3,2),(4,1)])
def test_count_bits(test_input, expected):
    "Test count_bits"

    # Test
    result = count_bits(test_input)
    
    # Assert
    # 2 in binary is "10". That is one (1) bit
    assert result == expected


def test_parity():
    """The partiy of a binary word is 1 
    if the number of 1s in the word is odd. 
    Otherwise it is 0.
    
    For example the parity of 1011 is 1, and
    the parity of 1001 is 0."""

    # Set up
    parity_one = 7
    # This is "111" in binary

    parity_zero = 3
    # This is "11" in binary

    # Act
    result_odd = parity(parity_one)
    result_even = parity(parity_zero)

    # Assert
    assert result_odd == 1
    assert result_even == 0


