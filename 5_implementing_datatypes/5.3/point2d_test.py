from point2d import make_point, to_string, move

p1 = make_point(0, 0)
p2 = p1

move(p1, 1, 1)

print(to_string(p2))

move(p2, 3, 3)

print(to_string(p2))