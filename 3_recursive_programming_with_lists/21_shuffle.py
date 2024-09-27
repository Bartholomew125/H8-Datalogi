def shuffle(v: list, w: list) -> list:
    """
    Takes two list, and alternates appending 
    each element to new list 
    """
    if v == [] or w == []:
        return w + v
    return [v[0]] + shuffle(w, v[1:])