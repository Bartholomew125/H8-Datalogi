def is_palindrome(n: int) -> bool:
    """ Returns the validity of n being a palindrome
    >>> is_palindrom(123)
    False
    >>> is_palindrome(34543)
    True
    """
    return n == _is_palindrome(n,0)

def _is_palindrome(n: int,rev: int):
    """ Makes a reverse copy of n and returns it
    """
    if n == 0:
        return rev
    
    rev = rev*10 + n%10
    
    return _is_palindrome(n//10,rev)
