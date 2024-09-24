v = [2,3,5,1]
def length(v:list) -> int:
    """
    The number of elements in v
    """
    if v == []:
        return 0
    else:
        return 1+length(v[1:])
print(length(v))
