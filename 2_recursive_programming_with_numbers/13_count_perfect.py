def count_perfect(n: int) -> int:
    """ Returns the number of perfect numbers smaller than n
    >>> count_perfect(30)
    2
    >>> count_perfect(10)
    1
    """
    if n == 0:
        return 0
    else:
        return (1 if is_perfect(n) else 0) + count_perfect(n-1)

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
