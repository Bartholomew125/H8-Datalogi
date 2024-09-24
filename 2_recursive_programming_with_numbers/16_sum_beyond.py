def sum_beyond(k: int) -> int:
    """Returns an n, where the sum of natural integers less than or equal to n,
    is less than or equal to k.
    >>> sum_beyond(10)
    4
    >>> sum_beyond(100)
    13
    """
    return _sum_beyond(k,1)

def _sum_beyond(k: int,n: int) -> int:
    """ Finds an n that works
    """
    if sum_up_to(n) > k:
        return 0
    else:
        return 1+_sum_beyond(k,n+1)

def sum_up_to(n: int) -> int:
    """ Returns the sum of all positive integers less than n
    >>> sum_up_to(10)
    55
    >>>
    sum_up_to(1)
    1
    """
    if n == 0:
        return 0
    else:
        return n + sum_up_to(n-1)
