n = int(input("Give me a number: "))
def one_to_n(n:int) -> list[int]:
    """
    Returns a list with the n numbers from 1 to n
    """
    if n <= 0:
        return []
    else: 
        return one_to_n(n-1)+[n]
print(one_to_n(n))  