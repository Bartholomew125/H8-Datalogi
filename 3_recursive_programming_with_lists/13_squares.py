def squares(n: int) -> list:
    """ Returns a list of the squares of all natural numbers up to n
    >>> squares(9)
    [1,4,9,16,25,36,49,64,81]
    >>> squares(1)
    [1]
    """
    return _squares(1, n, [])

def _squares(x: int, n: int, v: list) -> list:

    if x == n + 1:
        return v
    
    else:
        v.append(x**2)
        return _squares(x + 1, n, v)
