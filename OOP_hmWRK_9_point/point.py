import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        res = Point(self.x + other.x, self.y + other.y)
        return res

    def __sub__(self, other):
        res = Point(self.x - other.x, self.y - other.y)
        return res

    def __str__(self):
        return str(self.x) + " " + str(self.y)


class Triangle:

    def __init__(self, p01, p02, p03):
        self.p1 = p01
        self.p2 = p02
        self.p3 = p03

    def area(self):
        area = 1 / 2 * abs(
            (self.p2.x - self.p1.x) * (self.p3.y - self.p1.y) - (self.p3.x - self.p1.x) * (
                    self.p2.y - self.p1.y))

        return area

    def perimetr(self):
        per = math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2) + math.sqrt(
            (self.p3.x - self.p2.x) ** 2 + (self.p3.y - self.p2.y) ** 2) + math.sqrt(
            (self.p3.x - self.p1.x) ** 2 + (self.p3.y - self.p1.y) ** 2)
        return per

    def editP1(self, newx, newy):
        self.p1.x = newx
        self.p1.y = newy

    def editP2(self, newx, newy):
        self.p2.x = newx
        self.p2.y = newy

    def editP3(self, newx, newy):
        self.p3.x = newx
        self.p3.y = newy


p1 = Point(4, 2)
p2 = Point(3, 1)
p3 = Point(2, 2)
tr1 = Triangle(p1, p2, p3)
# print(tr1.area())
# print(tr1.perimetr())
# print(p3+p2)
# print(p3-p2)
# print(tr1.p1, tr1.p2, tr1.p3)
# tr1.editP1(10, 12)
# print(tr1.p1, tr1.p2, tr1.p3)
