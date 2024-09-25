def set_equals(v: list,w: list) -> bool:
    """ Determines wether the sets v and w are equal sets
    >>> set_equals([1,1,2,3],[1,2,3])
    True
    >>> set_equals([],[1])
    False
    """
    if v == w:  # If v and w are empty sets
        return True
    elif subset(v,w) and subset(w,v):
        return True
    else:
        return False

def subset(v: list,w: list) -> bool:
    """ Determines wether v is a subset of w, provided that v != []
    >>> subset([1,2],[1,2,3])
    True
    >>> subset([1,2,3],[2,3,4])
    False
    """
    if v == []:
        return True
    elif member(v[0],w):
        return subset(v[1:],w)
    else:
        return False

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
