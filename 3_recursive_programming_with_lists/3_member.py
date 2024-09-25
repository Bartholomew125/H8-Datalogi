def member(x: any,v: list) -> bool:
    """ Determines wether x is in v
    >>> member(1,[1,2,3])
    True
    >>> member(0,[3,4,5])
    False
    """
    if v == []:
        return False
    elif v[0] == x:
        return True
    else:
        return member(x,v[1:])
