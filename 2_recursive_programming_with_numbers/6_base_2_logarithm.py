def logarithm(n: int) -> int:
    """Returns the integer base-2 logarithm of n.
    
    >>logarithm(9)
    3
    >>logarithm(8)
    3
    >>logarithm(1)
    0
    """
    if n == 1:
        return 0
    else:
        return logarithm(n//2) + 1
    
