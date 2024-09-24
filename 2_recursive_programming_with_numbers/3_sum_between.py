def sum_between(m:int, n:int) -> int:
    """ Returns the sum of all integers between m and n
    >>> sum_between(3,8)
    22
    >>> sum_between(9,9)
    0
    """
    if m >= n-1:
        return 0
    else:
        return n-1 + sum_between(m,n-1)
    
