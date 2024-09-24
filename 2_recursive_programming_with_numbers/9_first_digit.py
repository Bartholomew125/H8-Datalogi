def first_digit(n: int,k: int=10) -> int:
    """ Returns the first digit of the decimal representation of n in base k
    >>> first_digit(1234)
    1
    >>> first_digit(8,3)
    2
    """
    if n < k:
        return n
    else:
        return first_digit(n//k,k)
    
    
