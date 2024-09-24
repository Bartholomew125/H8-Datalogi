def is_palindrome(n: int) -> bool:
    """ Check if n is a palindrome
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(123)
    False
    """
    L = _is_palindrome(n) # split n digits to list
    if L == L[::-1]: # checks if palindrome
        return True
    else:
        return False

def _is_palindrome(n: int, L: list = None) -> list:
    """
    Helper function for is_palindrome.
    recursively appends each digit of n, to list.
    """
    if L == None: # Creates empty list, for first recursion
        L = []
    if n == 0:
        return L
    else:
        L.append(n % 10) # Appends last digit to list
        return _is_palindrome(n // 10, L) # Recursion call