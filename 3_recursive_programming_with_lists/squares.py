def _squares(n: int, k: int) -> list[int]:
    if ((k + 1)**2) <= n:
        return [(k + 1)**2] + _squares(n, k + 1)
    return []

def squares(n: int) -> list[int]:
    return _squares(n, 1)