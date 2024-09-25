def two_zeros(v: list[int]) -> bool:
    """ Checks wether v contains two consecutive zeros
    >>> two_zeros([1,2,6,2,5,0,0,2,3])
    True
    >>> two_zeros([1,1,1])
    False
    """
    if v == []:
        return False

    elif v[0] == 0 and v[1:] and v[1] == 0:
        return True
    
    else:
        return two_zeros(v[1:])
    
    return False
    
