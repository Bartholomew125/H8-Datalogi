def shuffle(v: list, w: list) -> list:
    """
    Takes two list, and alternates appending 
    each element to new list 
    """
    if v == []:
        return w
    elif w == []:
        return v
    return [v[0]] + shuffle(w, v[1:])