def length(v: list) -> int:
    """ Returns the length of v
    >>> length([1,5,2,3])
    4
    >>> length([])
    0
    """
    if v == []:
        return 0
    else:
        return 1 + length(v[1:])
    
