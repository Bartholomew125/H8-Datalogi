from opg_5_4_polygon import *
from opg_5_3_point2d import make_point

p1 = make_point(-39.82,-76.11)
p2 = make_point(1.68,-1.13)
p3 = make_point(58.91,-44.53)

points = [p1,p2,p3]

polle = make_polygon(points)

print(to_string(polle))

print(perimeter(polle))

print(nearest(polle))

print(longest_side(polle))
