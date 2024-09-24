def double_factorial(n: int) -> int:
    """ Returns the double factorial of n
    >>> double_factorial(5)
    15
    >>>  double_factorial(8)
    384
    """
    if n <= 1:
        return 1
    else:
        return n * double_factorial(n-2)
