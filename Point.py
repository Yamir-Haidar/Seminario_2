import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_coordinate_x(self) -> int:
        return self.x

    def get_coordinate_y(self) -> int:
        return self.y

    def get_location(self) -> str:
        return f"( {self.x},{self.y} )"

    def quadrant(self) -> str:
        quadrant: str

        if self.x == 0 and self.y != 0:
            quadrant = "Sobre el eje Y"

        elif self.x != 0 and self.y == 0:
            quadrant = "Sobre el eje X"

        elif self.x == 0 and self.y == 0:
            quadrant = "En el origen de coordenadas"

        elif self.x > 0 and self.y > 0:
            quadrant = "Cuadrante 1"

        elif self.x < 0 < self.y:
            quadrant = "Cuadrante 2"

        elif self.x < 0 and self.y < 0:
            quadrant = "Cuadrante 3"

        else:
            quadrant = "Cuadrante 4"

        return quadrant

    def vector(self, point) -> str:
        return f"( {point.get_coordinate_x() - self.x},{point.get_coordinate_y() - self.y} )"

    def distance(self, point) -> str:
        return f"{math.sqrt(pow(point.get_coordinate_x() - self.x, 2) + pow(point.get_coordinate_y() - self.y, 2))}"
