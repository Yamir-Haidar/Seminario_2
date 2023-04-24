import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return type(other) == Point and self.y == other.y and self.x == other.x

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def quadrant(self) -> str:
        quadrant: str

        if self.x == 0 and self.y != 0:
            quadrant = "eje Y"

        elif self.x != 0 and self.y == 0:
            quadrant = "eje X"

        elif self.x == 0 and self.y == 0:
            quadrant = "origen de coordenadas"

        elif self.x > 0 and self.y > 0:
            quadrant = "cuadrante 1"

        elif self.x < 0 < self.y:
            quadrant = "cuadrante 2"

        elif self.x < 0 and self.y < 0:
            quadrant = "cuadrante 3"

        else:
            quadrant = "cuadrante 4"

        return quadrant

    def vector(self, point) -> str:
        return f"({point.get_x() - self.x},{point.get_y() - self.y})"

    def distance(self, point) -> float:
        return round(math.sqrt(pow(point.get_x() - self.x, 2) + pow(point.get_y() - self.y, 2)), 5)

    @staticmethod
    def farthest_from_origin(*args):
        result = args[0]
        result_value = Point().distance(result)
        for i in args:
            temporal_value = Point().distance(i)
            if temporal_value > result_value:
                result = i
        return result


