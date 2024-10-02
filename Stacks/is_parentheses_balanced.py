import Stack

def is_parentheses_balanced(expression: str) -> bool:
    """
    Checks if parentheses are balanced.
    >>> is_parentheses_balanced("{([Hello])}")
    True
    >>> is_parentheses_balanced("{([})]")
    False
    >>> is_parentheses_balanced("((Hello)")
    False
    """
    stack = Stack.make_stack()
    
    # Defining parentheses pairs
    parentheses = {
        '}': '{',
        ')': '(',
        ']': '[',
    }

    # Goes trough each char in expression and appends open parentheses,
    # and checks if parentheses open and close in order
    for char in expression:
        # If char is open parentheses, append it to stack
        if char in parentheses.values():
            Stack.add(stack, char)
        
        # If char is a closing parenthesis, check if last parenthesis was of same type
        # else return False
        elif char in parentheses.keys():
            # Check if closing parenthesis match last parenthesis
            if Stack.is_empty(stack) or Stack.top(stack) != parentheses[char]:
                return False
                
            # Removing last element of stack
            Stack.pop(stack)

    # Return True if stack is empty
    return Stack.is_empty()