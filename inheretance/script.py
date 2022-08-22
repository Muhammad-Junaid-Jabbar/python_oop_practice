class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print("(" + str(self.x) + "," + str(self.y) + ")")

    def move(self):
        self.x += 1
        self.y += 1


class point_opt(point):
    def __init__(self, x, y, z=1):
        super().__init__(x, y)
        self.z = z

    def __add__(self, p):
        return point_opt(self.x + p.x, self.y + p.y + self.z + p.z)

    def __mul__(self, p):
        return point(self.x * p.x, self.x * p.x)

    def __sub__(self, p):
        return point(self.x - p.x, self.x - p.x)

    def print(self):
        print("(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")")


p1 = point_opt(1, 2)
p2 = point_opt(2, 1)
p1.print()
p2.print()
p1.move()
p1.print()
p3 = p1 + p2
p3.print()
p4 = p1 * p3
p4.print()
