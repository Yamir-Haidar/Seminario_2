from Point import Point as Point

point1 = Point(-5, -6)
point2 = Point(2, -1)

print(point1.get_coordinate_x())
print(point1.get_coordinate_y())

print(point1.get_location())

print(point2.get_coordinate_x())
print(point2.get_coordinate_y())

print(point2.get_location())

print(point1.quadrant())
print(point2.quadrant())

print(f"Vector: {point1.vector(point2)}\n")

print(f"Vector: {point2.vector(point1)}\n")

print(f"Distancia: {point1.distance(point2)}\n")
print(f"Distancia: {point2.distance(point1)}")
