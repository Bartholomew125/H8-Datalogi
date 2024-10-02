from dataclasses import dataclass

@dataclass
class Stack:
    stack: list[str]

def make_stack() -> Stack:
    return Stack()

def copy(s: Stack) -> Stack:
    return s.stack

def is_empty(s: Stack) -> bool:
    return s.stack == []

def top(s: Stack) -> str:
    return s.stack[-1]

def pop(s: Stack) -> None:
    s.stack.pop()

def add(s: Stack, value: str) -> None:
    s.stack.append(value)

def print(s: Stack) -> None:
    print(s.stack)