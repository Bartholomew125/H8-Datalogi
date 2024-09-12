n = int(input("Give me a number: "))
def print_stars(n:int) -> None:
    """
    Prints a line with n-stars
    """
    if n > 0:
        print('*')
        print_stars(n-1)
print(print_stars(n))
