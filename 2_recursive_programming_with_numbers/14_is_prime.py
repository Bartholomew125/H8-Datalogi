def is_prime(n: int) -> bool:
    """ Test if n is prime
    >>> is_prime(301)
    False
    >>> is_prime(97)
    True
    """
    return _is_prime(n,n) == 2

def _is_prime(n: int,m: int) -> int:
    """ Counts divisors of n
    """
    if m == 0:
        return 0
    elif n%m == 0:
        return 1+_is_prime(n,m-1)
    else:
        return _is_prime(n,m-1)
