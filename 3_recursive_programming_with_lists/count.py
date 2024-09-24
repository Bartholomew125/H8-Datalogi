def count(x: any, v: list) -> int:
    if v ==[]:
        return 0
    elif x == v[0]:
        return 1 + count(x, v[1:])
    count(x, v[1:])