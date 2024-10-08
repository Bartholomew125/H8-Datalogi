from dataclasses import dataclass


# Decorator
@dataclass
class Point2d:
    x: float
    y: float


def make_point(x: float, y: float) -> Point2d:
    """Returns a new instance of point2d with the given coordinates."""
    return Point2d(x, y)


def move(p: Point2d, dx: float, dy: float) -> None:
    """Move the point p according to the vector (dx, dy)."""
    p.x = p.x + dx
    p.y = p.y + dy

def distance_to_origin(p: Point2d) -> float:
    """Returns p's distance to the origin."""
    return ((p.x*p.x) + (p.y*p.y)) ** (1/2)


def distance(p1: Point2d, p2: Point2d) -> float:
    """Returns the distance between p1 and p2."""
    return ((p2.x - p1.x)*(p2.x - p1.x)  + 
            (p2.y - p1.y)*(p2.y - p1.y)) ** (1/2)


def equals(p1: Point2d, p2: Point2d) -> bool:
    """Determins wether p1 and p2 represents the same point."""
    return (p1.x == p2.x and p1.y == p2.y)


def copy(p: Point2d) -> Point2d:
    """Returns a copy of the point."""
    return Point2d(p.x, p.y)


def to_string(p: Point2d) -> str:
    """Returns a textual representation of p."""
    return f"({p.x}, {p.y})"
