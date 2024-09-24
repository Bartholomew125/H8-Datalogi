def count_primes(n: int) -> int:
    """ Returns the number of primes smaller than n, provided that n > 1
    >>> count_primes(20)
    8
    >>> count_primes(37)
    11
    """
    if n == 1:
        return 0
    else:
        return (1 if is_prime(n-1) else 0) + count_primes(n-1)

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
