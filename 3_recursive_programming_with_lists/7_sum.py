def sum(v: list[int]) -> int:
    """ Returns the sum of all values in v
    >>> sum([1,2,3,4])
    10
    >>> sum([5,9,10])
    24
    """
    if v == []:
        return 0
    else:
        return v[0] + sum(v[1:])
