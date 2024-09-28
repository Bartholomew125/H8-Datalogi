def is_parentheses_balanced(expression: str) -> bool:
    """
    Checks if parentheses are balanced.
    >>> is_parentheses_balanced("{[Hel(lo)]Wrld}")
    True
    >>> is_parentheses_balanced("{[(Hello world)}]")
    False
    >>> is_parentheses_balanced("((Hello)")
    False
    """
    # Defining parentheses and stack
    stack = []
    parentheses = {
        '}': '{',
        ')': '(',
        ']': '[',
    }

    # Goes expression and appends open parentheses, and checks if closing parentheses match last parentheses
    for char in expression:
        # If open parentheses, append it to stack
        if char in parentheses.values():
            stack.append(char)
        
        # if closing parentheses match last parentheses, remove last element of stack
        # else return False
        elif char in parentheses.keys():
            # Check closing parentheses match last parentheses
            if not stack or stack[-1] != parentheses[char]:
                return False
            
            # Removing last element of stack
            stack.pop()

    # Return True if stack is empty
    return not stack