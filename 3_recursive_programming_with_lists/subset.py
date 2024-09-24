def subset(v: list, w: list) -> bool:
    if v == []:
         return True
    elif w != [] and v[0] == w[0]:
        return True and subset(v[1:], w[1:])
    return False