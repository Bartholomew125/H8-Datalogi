def max(v: list[int]) -> int:
    """ Returns the largest element in the non-empty list v
    >>> max([1,7,3,5])
    7
    >>> max([0])
    0
    """
    return _max(v,v[0])

def _max(v: list[int], x: int) -> int:
    
    if v == []:
        return x
    
    elif v[0] > x:
        x = v[0]
        return _max(v[1:],x)
    
    else:
        return _max(v[1:],x)
