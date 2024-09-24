def lcm(m: int,n: int) -> int:
    """ Returns the least common multiple of m and n using gcd
    >>> lcm(7,4)
    28
    >>> lcm(128,80)
    640
    """
    GCD = gcd(m,n)
    if GCD == 1:
        return m*n
    else:
        return int(max(m,n)/GCD) * min(m,n)

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
