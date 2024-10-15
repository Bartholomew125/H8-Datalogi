import point2d
import polygon

def run(func: callable, expected: any, *args) -> bool:
    """ Run functions and reads if output is same as expected, 
        if not returns False and print error messege.
        run(func, expectecd_output, args)"""
    if func(*args) != expected:
        print(f"Error with: {func.__name__}({', '.join(map(str, args))})")
        print(f"Expected {expected}, got {func(*args)}")
        return False
    else:
        return True
    
a = point2d.make_point(0, 0)
b = point2d.make_point(0, 2.0)
c = point2d.make_point(2.0, 2.0)
d = point2d.make_point(2.0, 0)
square = polygon.make_polygon([a, b, c, d])
run(polygon.perimeter, 8, square)
run(polygon.nearest, a, square)
print(polygon.to_string(square))

a = point2d.make_point(0, 0)
b = point2d.make_point(0, 2.0)
c = point2d.make_point(2.0, 3.0)
d = point2d.make_point(2.0, 0)
square = polygon.make_polygon([a, b, c, d])
run(polygon.longest_side, 3.0, square)
run(polygon.vertices_in_quadrant, 1, square, 1)
print(polygon.to_string(square))

a = point2d.make_point(1, 1)
b = point2d.make_point(1, 2.0)
c = point2d.make_point(2.0, 3.0)
d = point2d.make_point(2.0, 1)
square = polygon.make_polygon([a, b, c, d])
run(polygon.vertices_in_quadrant, 4, square, 1)
run(polygon.is_rectangle, True, square)
run(polygon.is_quadrilateral, True, square)
print(polygon.to_string(square))

a = point2d.make_point(1, 1)
b = point2d.make_point(2, 1)
c = point2d.make_point(3, 1)
d = point2d.make_point(4, 1)
e = point2d.make_point(4, 2)
f = point2d.make_point(1, 2)
square = polygon.make_polygon([a, b, c, d, e, f])
run(polygon.is_quadrilateral, True, square)
run(polygon.is_triangle, False, square)
print(polygon.to_string(square))