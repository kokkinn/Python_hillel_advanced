import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        res = Point(self.x + other.x, self.y + other.y)
        return res

    def __str__(self):
        return str(self.x) + " " + str(self.y)


p1 = Point(4, 5)
p2 = Point(3, 6)
p3 = Point(2, 4)


class Triangle:

    def __init__(self):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

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
        self.p1.x = newx
        self.p1.y = newy

    def editP3(self, newx, newy):
        self.p1.x = newx
        self.p1.y = newy


tr1 = Triangle()
print(tr1.area())
print(tr1.perimetr())
tr1.editP1(2, 1)
tr1.editP2(2, 3)
print(tr1.p1.x)
print(tr1.p2.y)
