from Point import Point
from Rectangle import Rectangle

# Experimentacion

# Inciso 1
a = Point(2, 3)
b = Point(5, 5)
c = Point(-3, -1)
d = Point()
print("Inciso 1")
print("Las coordenadas de A son:", a)
print("Las coordenadas de B son:", b)
print("Las coordenadas de C son:", c)
print("Las coordenadas de D son:", d)

# Inciso 2
print("\nInciso 2")
print("El punto A pertenece al", a.quadrant())
print("El punto C pertenece al", c.quadrant())
print("El punto D pertenece al", d.quadrant())

# Inciso 3
print("\nInciso 3")
print("El vector AB es:", a.vector(b))
print("El vector BA es:", b.vector(a))

# Inciso 4
print("\nInciso 4")
print("La distancia del punto A al B es:", a.distance(b))
print("La distancia del punto B al A es:", b.distance(a))

# Inciso 5
print("\nInciso 5")
value = Point.farthest_from_origin(a, b, c)
print("El punto mas cercano al origen es:", "c" if value == c else "a" if value == a else "b",
      "y sus coordenadas son:", value)

# Inciso 6
print("\nInciso 6")
r = Rectangle(a, b)
print("Se crea el rectangulo satisfactoriamente" if r == Rectangle(a, b) else "Error")

# Inciso 7
print("\nInciso 7")
print("La base es:", r.base())
print("La altura es:", r.height())
print("El area es:", r.area())
