from dataclasses import dataclass
from opg_5_3_point2d import Point2d, distance, distance_to_origin

@dataclass
class Polygon:
    verticies: list[Point2d]

def make_polygon(v: list[Point2d]) -> Polygon:
    """ Returns a new polygon from the list of verticies.
    """
    return Polygon(v)#🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮

def copy(p: Polygon) -> Polygon:
    """ Returns a copy of p diddy.
    """
    return Polygon(p.verticies)

def perimeter(p: Polygon) -> float:
    """ Returns the perimiter of p.
    """
    return _perimeter(p) + distance(p.verticies[0],p.verticies[-1])

def _perimeter(p: Polygon) -> float:
    if len(p.verticies) <= 1:
        return 0
    else:
        return distance(p.verticies[0],p.verticies[1]) + _perimeter(Polygon(p.verticies[1:]))
    
def nearest(p: Polygon) -> Point2d:
    """ Returns the vertex of p that is closest to the origin.
    """
    if len(p.verticies) == 1:
        return p.verticies[0]
    elif distance_to_origin(p.verticies[0]) < distance_to_origin(nearest(Polygon(p.verticies[1:]))):
        return p.verticies[0]
    else:
        return nearest(Polygon(p.verticies[1:]))

def longest_side(p: Polygon) -> float:
    """ Returns the length of p's longest side.
    """
    return _longest_side(p.verticies, p.verticies[0])
   
def _longest_side(v: list[Point2d], p0: Point2d) -> float:
    if len(v) <= 1:
        return distance(v[0], p0)
    elif distance(v[0], v[1]) >= _longest_side(v[1:], p0):
        return distance(v[0], v[1])
    else:
        return _longest_side(v[1:], p0)

def to_string(p: Polygon) -> str:
    """Returns a textual representation of p.
    """
    return "".join([f"({v.x},{v.y}), " for v in p.verticies])[:-2]