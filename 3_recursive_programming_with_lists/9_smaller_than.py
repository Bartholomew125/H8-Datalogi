def smaller_than(n: int, v: list) -> int:
    """Counts how many elements of v are strictly smaller than n
    >>> smaller_than(2, [0,1,2,3])
    2
    >>> smaller_than(0, [1,2,3])
    0
    """
    if v == []:
        return 0
    elif v[0] < n:
        return 1 + smaller_than(n, v[1:])
    else:
        return smaller_than(n, v[1:])
