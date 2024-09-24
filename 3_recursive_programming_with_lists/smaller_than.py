def smaller_than(n: int, v: list) -> int:
    if v == []:
        return 0
    elif n < v[0]:
        return 1 + smaller_than(n, v[1:])
    return smaller_than(n, v[1:])