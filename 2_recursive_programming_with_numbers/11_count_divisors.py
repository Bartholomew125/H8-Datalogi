def count_divisors(n: int) -> int:
    """ Return the number of divisors of n
    >>> count_divisors(20)
    5
    >>> count_divisors(11)
    2
    """
    return _count_divisors(n,n)

def _count_divisors(n: int, m: int) -> int:
    """ Return amount of divisors in n
    """
    if m == 0:
        return 0
    elif n%m == 0:
        return 1 + _count_divisors(n,m-1)
    else:
        return _count_divisors(n,m-1)
