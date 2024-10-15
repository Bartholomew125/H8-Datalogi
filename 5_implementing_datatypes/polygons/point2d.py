from dataclasses import dataclass
import math

@dataclass
class point2D:
    x: float
    y: float

def make_point(x: float, y: float) -> point2D:
    """ Returns instance of point2D"""
    return point2D(x= x, y= y)

def move(p: point2D, dx: float, dy: float) -> None:
    """ Moves point2D by dx and dy"""
    p.x += dx
    p.y += dy

def distance_to_origin(p: point2D) -> float:
    """ Returns distance from point to (0, 0)"""
    return math.sqrt(p.x * p.x + p.y *p.y)

def distance(p1: point2D, p2: point2D) -> float:
    """ Returns distance between two points"""
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def equals(p1: point2D, p2: point2D) -> bool:
    """ Returns rether two points have same coordinates"""
    return (p1.x == p2.x and
            p1.y == p2.y)

def copy(p: point2D) -> point2D:
    """ Returns point with same x and y values as p"""
    return point2D(p.x, p.y)

def to_string(p: point2D) -> str:
    """ Returns point as str 
    to_string(2, 5)
    >>>(2, 5)
    """
    return f"({p.x}, {p.y})"

def x(p: point2D) -> float:
    return p.x

def y(p: point2D) -> float:
    return p.y

def is_collinear(p1: point2D, p2: point2D, p3: point2D) -> bool:
    """ Solving for determinant of a 3x3 matrix using magic.
    When the determinant is 0, the three points are collinear"""
    return p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y) == 0

def in_quadrant(p: point2D, quadrant: int) -> bool:
    switch = {
        1: lambda x, y: x > 0 and y > 0,
        2: lambda x, y: x < 0 and y > 0,
        3: lambda x, y: x < 0 and y < 0,
        4: lambda x, y: x > 0 and y < 0
    }
    return switch.get(quadrant)(p.x, p.y)