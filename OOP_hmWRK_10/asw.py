class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(Shape):
    pass


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.radius = r

    def contains(self, point):
        if (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.radius ** 2:
            return True
        else:
            return False

    def __contains__(self, item):
        return self.contains(item)


po1 = Point(0, 0)
po2 = Point(1, 1)
Circle1 = Circle(2, 2, 5)
Circle2 = Circle(10, 10, 3)
print(Circle1.contains(po1))
print(po2 in Circle2)
print(po1 in Circle1)
