from Point import Point


class Rectangle:
    def __init__(self, initial=Point(0, 0), final=Point(0, 0)):
        self.initial = initial
        self.final = final

    def __eq__(self, other):
        return type(other) == Rectangle and self.initial == other.initial and self.final == other.final

    def base(self):
        return Point(x=self.initial.get_x()).distance(Point(x=self.final.get_x()))

    def height(self):
        return Point(y=self.initial.get_y()).distance(Point(y=self.final.get_y()))

    def area(self):
        return self.base() * self.height()
