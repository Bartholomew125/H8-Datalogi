"""
Write a functionsum_up_to(n: int) -> int that returns the sum of the natural 
numbers up to n.
"""
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
