def intersect(v: list, w: list) -> list:
    """ Returns a list containing the elements that occur both in v and w
    >>> intersect([1,2,3],[2,3,4])
    [2,3]
    >>> intersect([1,5,5],[5,6])
    [5]
    >>> intersect([],[])
    []
    """
    return _intersect(v,w,[])

def _intersect(v: list, w: list, result: list) -> list:
    
    if v == []:
        return []
    
    elif not get_member(v[0],result):
        
        result += get_member(v[0],w)
        print(type(v),type(w),type(result))
        result = result + _intersect(v[1:],w,result)
        
    
    return result

def get_member(x: any, w: list) -> list:
    """ Returns the x in a list if its in w otherwise returns an empty list
    >>> member(1,[1,2,3])
    [1]
    >>> member(0,[3,4,5])
    []
    """
    if w == []:
        return []
    elif w[0] == x:
        return [x]
    else:
        return get_member(x,w[1:])
