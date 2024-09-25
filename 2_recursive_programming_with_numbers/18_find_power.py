def find_power(k: int) -> int:
    """ Returns the first n where the first character of 2^n is k
    provided that k is a single digit
    >>> find_power(1)
    0
    >>> find_power(4)
    2
    """
    return _find_power(k,0)

def _find_power(k: int,n: int) -> int:
    if k == first_digit(2**n):
        return n
    else:
        return _find_power(k,n+1)

def first_digit(n: int) -> int:
    """ Returns the first digit of the decimal representation of n in base k
    >>> first_digit(1234)
    1
    """
    if n < 10:
        return n
    else:
        return first_digit(n//10)
    
    
