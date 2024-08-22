import pytest
import timeit

from primitives import count_bits, parity, parity_better



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


def test_partiy_better():
    """This should give us a faster result"""
    # Set up
    parity_one = 7
    # This is "111" in binary

    parity_zero = 3
    # This is "11" in binary

    # Act
    result_odd = parity_better(parity_one)
    result_even = parity_better(parity_zero)

    # Assert
    assert result_odd == 1
    assert result_even == 0    


def test_time_parity():
    result_parity = timeit.timeit("parity(345)", "from primitives import parity, SOME_INT")
    result_parity2 = timeit.timeit("parity_better(345)", "from primitives import parity_better, SOME_INT")
    print(result_parity, result_parity2)