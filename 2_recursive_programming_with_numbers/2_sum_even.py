def sum_even(n: int) -> int:
    """
    Returns the sum up to an even number n.

    >>sum_even(8)
    20
    >>sum_even(0)
    0
    """
    if n < 0:
        return 0
    elif n % 2 != 0:
        return sum_even(n - 1)
    else:
        return n + sum_even(n - 2)
    
