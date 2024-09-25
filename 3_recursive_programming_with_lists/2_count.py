def count(x: any,v: list) -> int:
    """ Returns the number of times x occurs in v
    >>> count(1,[1,2,3,2,1,1])
    3
    >>> count(2,[0,1,3])
    0
    """
    if v == []:
        return 0
    elif v[0] == x:
        return 1 + count(x,v[1:])
    else:
        return count(x,v[1:])
