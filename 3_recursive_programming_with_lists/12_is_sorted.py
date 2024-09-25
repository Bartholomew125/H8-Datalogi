def is_sorted(v: list[int]) -> bool:
    """ Checks wether a list v is sorted from smallest to largest
    >>> is_sorted([1,2,5,6])
    True
    >>> is_sorted([3,1,4,1,5])
    False
    """
    return _is_sorted(v, v[0])

def _is_sorted(v: list[int], x: int) -> bool:
    if v == []:
        return True
    
    elif x > v[0]:
        return False
    
    else:
        return _is_sorted(v[1:],v[0])
