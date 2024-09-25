def even_after_7(v: list[int]) -> int:
    """ Returns the amount of even number after the first occurence of 7 in v.
    Requires a 7 to be in v.
    >>> even_after_7([3,7,2,3,4,5,6])
    3
    >>> even_after_7([1,2,3,7])
    0
    """
    v = _even_after_7(v)
    return count_even(v)

def _even_after_7(v: list[int]) -> list:
    if v == []:
        return []
    elif v[0] == 7:
        return v[1:]
    else:
        return _even_after_7(v[1:])


def count_even(v: list) -> int:
    if v == []:
        return 0

    elif v[0]%2 != 0:
        return count_even(v[1:])
    
    else:
        return 1 + count_even(v[1:])
