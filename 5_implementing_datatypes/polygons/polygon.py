from dataclasses import dataclass
import point2d

@dataclass
class Polygon:
    vertices: list[point2d.point2D]

"""
Standard functions
"""
def make_polygon(vertices: list[point2d.point2D]) -> Polygon:
    """ Returns dataclass polygon, with list[point2D] of vertices."""
    return Polygon(vertices)

def copy(polygon: Polygon) -> Polygon:
    """ Returns copy of a given polygon"""
    return Polygon(polygon.vertices.copy())

def equals(polygon1: Polygon, polygon2: Polygon) -> bool:
    """ Returns rether two polygons are the same, disregaring collinear points"""
    vertices_set = set()
    
    # Saves last and second last index to prevent going out of range
    last_index = len(polygon1) - 1
    scnd_last_index = len(polygon1) - 2

    # adds all x, y's from polygon 1 as a tuple to vertices set
    for i, vertex in enumerate(polygon1.vertices):
        if (i == last_index and
            not point2d.is_collinear(vertex, polygon1.vertices[0], polygon1.vertices[1])):
                vertices_set.add((point2d.x(polygon1.vertices[0]), point2d.y(polygon1.vertices[0])))
        elif (i == scnd_last_index and
              not point2d.is_collinear(vertex, polygon1.vertices[i + 1], polygon1.vertices[0])):
                vertices_set.add((point2d.x(polygon1.vertices[i + 1], point2d.y(polygon1.vertices[i + 1]))))
        elif (i < scnd_last_index and
              not point2d.is_collinear(vertex, polygon1.vertices[i + 1], polygon1.vertices[i + 2])):
                vertices_set.add((point2d.x(polygon1.vertices[i + 1]), point2d.y(polygon1.vertices[i + 1])))
                

    # Saves last and second last index to prevent going out of range
    last_index = len(polygon2) - 1
    scnd_last_index = len(polygon2) - 2

    # Discards all x, y's from vertices set
    for i, vertex in enumerate(polygon2.vertices):
        if (i == last_index and
            not point2d.is_collinear(vertex, polygon2.vertices[0], polygon2.vertices[1])):
                vertices_set.discard((point2d.x(polygon2.vertices[0]), point2d.y(polygon2.vertices[0])))
        elif (i == scnd_last_index and
              not point2d.is_collinear(vertex, polygon2.vertices[i + 1], polygon2.vertices[0])):
                vertices_set.discard((point2d.x(polygon2.vertices[i + 1], point2d.y(polygon2.vertices[i + 1]))))
        elif (i < scnd_last_index and
              not point2d.is_collinear(vertex, polygon2.vertices[i + 1], polygon2.vertices[i + 2])):
                vertices_set.discard((point2d.x(polygon2.vertices[i + 1]), point2d.y(polygon2.vertices[i + 1])))

    # If the length of the vertices set is 0, then all vertices have been added, and removed again
    return len(vertices_set) == 0

def to_string(polygon: Polygon) -> str:
    """ Returns a polygon as a string.
       ex:
       ((0, 0), (0, 1), (1, 1), (1, 0))"""
    return "(".join((f"{point2d.to_string(vertex)}, ") for vertex in polygon.vertices) + ")"


"""
Length functions
"""
def perimeter(polygon: Polygon) -> float:
    """ Returns the perimeter of a polygon as a float"""
    perimeter = 0.0

    # Saves last index to avoid going out of range
    last_index = len(polygon.vertices) - 1

    # Adds up all the distances between the points
    for i, vertex in enumerate(polygon.vertices):

        # if last index, get distance from last to first vertex
        if i == last_index:
            perimeter += point2d.distance(vertex, polygon.vertices[0])

        # Else, get distance from current to next vertex
        else:
            perimeter += point2d.distance(vertex, polygon.vertices[i + 1])

    # Returns final perimeter
    return perimeter

def longest_side(polygon: Polygon) -> float:
    """ Returns the length of longest side of a polygon"""

    # Filters collinear points from polygon
    filtered_polygon = _filter_collinear_points(polygon)

    # Saves last index to avoid going out of range
    last_index = len(filtered_polygon.vertices) - 1

    # Compares distances between the points, saves largest
    longest_side = point2d.distance(filtered_polygon.vertices[0], filtered_polygon.vertices[1])
    for i, vertex in enumerate(filtered_polygon.vertices):

        # If at last index, get distance from last to first vertex
        if (i == last_index and
            point2d.distance(vertex, filtered_polygon.vertices[0]) > longest_side):
                longest_side = point2d.distance(vertex, filtered_polygon.vertices[0])

        # Else, compare distance of current to next vertex
        elif (i < last_index and
              point2d.distance(vertex, filtered_polygon.vertices[i + 1]) > longest_side):
                longest_side = point2d.distance(vertex, filtered_polygon.vertices[i + 1])

    # Returns longest distance
    return longest_side


"""
Point functions
"""
def nearest(polygon: Polygon) -> point2d.point2D:
    """ Returns nearest vertex to origin (0, 0)"""
    nearest = polygon.vertices[0]

    # Compares all distances to origin for all points in polygon, saves lowest
    for vertex in polygon.vertices:
        if point2d.distance_to_origin(vertex) < point2d.distance_to_origin(nearest):
            nearest = vertex

    # Return lowest distance to origin
    return nearest

def move(polygon: Polygon, dx: float, dy: float) -> None:
    """ Moves the whole polygon by dx and dy"""

    # Moves every vertex by dx and dy
    for vertex in polygon.vertices:
        point2d.move(vertex, dx, dy)

def vertices_in_quadrant(polygon: Polygon, quadrant: int) -> int:
    """ Returns number of vertices of a polygon in a given quadrant.
        x = 0 and y = 0 is in no quadrant"""
    vertices_in_quadrant = 0

    # Counts vertices in a given quadrant
    for vertex in polygon.vertices:
        if point2d.in_quadrant(vertex, quadrant): 
            vertices_in_quadrant += 1

    # Returns number of vertices in the quadrant
    return vertices_in_quadrant


"""
Boolean functions
"""
def is_triangle(polygon: Polygon) -> bool:
    """ Returns rether a given polygon is a triangle"""
    corners = 0

    # Save last and second last index to avoid going out of range
    last_index = len(polygon.vertices) - 1
    scnd_last_index = len(polygon.vertices) - 2

    # Counts number of corners in the polygon
    for i, vertex in enumerate(polygon.vertices):

        # If number of corners is above 3, returns False
        if i > 3:
            return False
        
        # If last index, compare collinearity of current, first and second vertex
        elif (i == last_index and
            not point2d.is_collinear(vertex, polygon.vertices[0], polygon.vertices[1])):
            corners += 1

        # if second last index, compare collinearity of current, last and first vertex
        elif (i == scnd_last_index and
            not point2d.is_collinear(vertex, polygon.vertices[i + 1], polygon.vertices[0])):
            corners += 1
        
        # else, compare collinearity of current, next and 2nd next vertex
        elif (i < scnd_last_index and
            not point2d.is_collinear(vertex, polygon.vertices[i + 1], polygon.vertices[i + 2])):
            corners += 1
    
    # Returns True if polygon has 3 corners
    return corners == 3

def is_rectangle(polygon: Polygon) -> bool:
    """ Returns rether a given polygon is a rectangle"""
    sides_set = set()

    # Copies polygon, but without collinear points
    filtered_polygon = _filter_collinear_points(polygon.vertices)

    # Saves last index to avoid going out of range
    last_index = len(filtered_polygon)

    # Adds each side length to sides set
    # If filterered polygon have more than 4 elements, then it's not a quadrilateral
    if len(filtered_polygon) == 4:

        # Adds each side length to sides set
        for i, vertex in enumerate(filtered_polygon):

            # If last index, get distance from last to first vertex
            if i == last_index:
                sides_set.add(point2d.distance(vertex, polygon.vertices[0]))

            # else, get distance from current to next vertex
            else:
                sides_set.add(point2d.distance(vertex, polygon.vertices[i + 1]))
    
    # Since a set can't contain duplicates, we should only get at max 2 different distances
    # if the polygon is a rectangle
    return len(sides_set) == 2 or len(sides_set) == 1

def is_quadrilateral(polygon: Polygon) -> bool:
    """ Checks rether a given polygon is a quadrilateral"""
    corners = 0

    # Saves last and second last index to avoid going out of range
    last_index = len(polygon.vertices) - 1
    scnd_last_index = len(polygon.vertices) - 2

    # Counts corners in polygon
    for i, vertex in enumerate(polygon.vertices):

        # If number of corners is above 4, returns False
        if corners > 4:
            return False
        
        # If at last index, compare collinearity of last, first and second vertex
        elif (i == last_index and
            not point2d.is_collinear(vertex, polygon.vertices[0], polygon.vertices[1])):
            corners += 1
        
        # If at second last index, compare collinearity of current, last and first vertex
        elif (i == scnd_last_index and
            not point2d.is_collinear(vertex, polygon.vertices[i + 1], polygon.vertices[0])):
            corners += 1
        
        # Else compare collinearity of current, and the next two vertices
        elif (i < scnd_last_index and
            not point2d.is_collinear(vertex, polygon.vertices[i + 1], polygon.vertices[i + 2])):
            corners += 1
    
    # Returns true if polygon has 4 corners
    return corners == 4


def _filter_collinear_points(polygon: Polygon) -> Polygon:
    """ Helper function, returns all collinear points from a """
    filtered_polygon = copy(polygon)

    # Saves last and second last index to avoid going out of range
    last_index = len(polygon.vertices) - 1
    scnd_last_index = len(polygon.vertices) - 2

    # Appends all collinear points indexes
    collinear_points = []
    for i, vertex in enumerate(polygon.vertices):

        # If last index, compare collinearity of last, first and second vertex
        if (i == last_index and
            point2d.is_collinear(vertex, polygon.vertices[0], polygon.vertices[1])):
            collinear_points.append(i + 1)

        # If second last index, compare collinearity of current, last and first vertex
        elif (i == scnd_last_index and
            point2d.is_collinear(vertex, polygon.vertices[i + 1], polygon.vertices[0])):
            collinear_points.append(i + 1)

        # Else compare collinearity of current, and the next two vertex
        elif (i < scnd_last_index and
            point2d.is_collinear(vertex, polygon.vertices[i + 1], polygon.vertices[i + 2])):
            collinear_points.append(i + 1)

    # Removes each collinear point from filltered polygon
    for index in reversed(collinear_points):
        filtered_polygon.vertices.pop(index)
    
    # Returns filttered polygon
    return filtered_polygon