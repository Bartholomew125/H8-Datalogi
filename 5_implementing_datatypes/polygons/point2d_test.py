import point2d

def run(func: callable, expect: any, *args) -> bool:
    if func(*args) != expect:
        print(f"Error with: {func.__name__}({', '.join(map(str, args))})")
        print(f"Expected {expect}, got {func(*args)}")
        return False
    else:
        return True
    
point1 = point2d.make_point(1.5, 1.5)
point2 = point2d.make_point(2.5, 2.5)

# equals()
run(point2d.equals, True, point1, point1)
run(point2d.equals, False, point1, point2)

# move()
run(point2d.move, None, point1, 1.0, 1.0)
run(point2d.to_string, "(2.5, 2.5)", point1)

point1 = point2d.make_point(3.0, 4.0)
point2 = point2d.make_point(6.0, 8.0)

# distance funcs
run(point2d.distance_to_origin, 5.0, point1)
run(point2d.distance, 5.0, point1, point2)

point1 = point2d.make_point(1.0, 1.0)
point2 = point2d.make_point(2.0, 2.0)
point3 = point2d.make_point(3.0, 3.0)

# Collinear funcs
run(point2d.is_collinear, True, point1, point2, point3)

run(point2d.move, None, point3, 1.0, 0)
run(point2d.is_collinear, False, point1, point2, point3)

# in_quadrant()
run(point2d.in_quadrant, True, point1, 1)
run(point2d.in_quadrant, False, point1, 2)