# Findes allerede i mappen, hvorved forklaring af løsning også ligger. 

def is_palindrome(n: int) -> bool:
    """ Check if n is a palindrome
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(123)
    False
    """
    num = _is_palindrome(n) # split n digits to list
    if num == num[::-1]: # checks if palindrome
        return True
    return False

def _is_palindrome(n: int, num: list = None) -> list:
    """
    Helper function for is_palindrome.
    recursively appends each digit of n, to list.
    """
    if num == None: # Creates empty list, for first recursion
        num = []
    if n == 0: # Halts recursion, when all digits in n, have been appended to list
        return num
    num.append(n % 10) # Appends last digit to list
    return _is_palindrome(n // 10, num) # Recursion call
