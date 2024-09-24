def member(x: any, v: list) -> bool:
    if v == []:
        return False
    return ((x == v[0]) or member(x, v[1:]))