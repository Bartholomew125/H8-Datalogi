def gcd(m: int,n: int) -> int:
    """ Returns the greatest common devisor using Euclids algorithm
    >>> gcd(25,30)
    5
    >>> gcd(47,19)
    1
    """
    if m == n:
        return m
    elif m < n:
        return gcd(m,n-m)
    elif m > n:
        return gcd(m-n,n)
