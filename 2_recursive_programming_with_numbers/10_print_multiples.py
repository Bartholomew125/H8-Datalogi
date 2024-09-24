def print_multiples(k: int =7, n: int = 500) -> None:
    """ Prints the multiple of k up to n (in ascendung order).

    >>print_multiples(7,21)
    7
    14
    21
    """
    _print_multiples(k, k, n)

def _print_multiples(k: int, m: int, n: int) -> None:
    """Prints multiples of k from m to n. Assume that m%k == 0.
    """
    if m <= n:
        print(m)
        _print_multiples(k, m+k, n)
    
