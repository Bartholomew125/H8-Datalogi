def sum(v: list[int]) -> int:
    if v == []:
        return 0
    return v[0] + sum(v[1:])