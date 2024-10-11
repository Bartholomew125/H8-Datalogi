from point2d import *

dx = 3
dy = 3
point = make_point(2, 4) # Test make_point method
point2 = make_point(3,7)
point3 = make_point(2,4)
point4 = make_point(2,4)
print(point)
move(point, dx, dy) # Test move method
print("Moved: " + str(point))
print("Distance to O: " + str(distance_to_origin(point))) # Test distance to origin method
print("Distance between p1 and p2: " + str(distance(point, point2))) # Test distance method
print("Check if point 1 and 2 is equal: " + str(equals(point, point2))) # Test equals method given a false statement
print("Check if point 3 and 4 is equal: " + str(equals(point3, point4))) # Test equals method given a true statement
print("Make a copy of point 1: " + str(copy(point))) # Test copy method
print("Turns the point to a string: " + to_string(point2)) # Test to string method