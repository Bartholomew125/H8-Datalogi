def is_perfect(n: int) -> bool:
    """ Test if n is a perfect number
    >>> is_perfect(20)
    False
    >>> is_perfect(6)
    True
    """
    return _is_perfect(n,n-1) == n

def _is_perfect(n: int, m: int) -> int:
    """ Return sum of divisors of n
    """
    if m == 0:
        return 0
    elif n%m == 0:
        return m + _is_perfect(n,m-1)
    else:
        return _is_perfect(n,m-1)
