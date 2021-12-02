class Point:
    def __init__(self, *args):
        self.coords = args
        self.dimension = len(args)

    def __str__(self):
        return f"Point{self.coords}"

    def __repr__(self):
        return str(self)

    @property
    def x(self):
        return self.coords[0]

    @property
    def y(self):
        return self.coords[1]

    @property
    def z(self):
        return self.coords[2]

    @property
    def w(self):
        return self.coords[3]

    def __add__(self, other):
        if not self.dimension == other.dimension:
            raise ValueError("Points have different dimensions")
        return Point(*[a + b for a, b in zip(self.coords, other.coords)])

    def __mul__(self, other):
        if not self.dimension == other.dimension:
            raise ValueError("Points have different dimensions")
        return Point(*[a * b for a, b in zip(self.coords, other.coords)])

    def __eq__(self, other):
        if not self.dimension == other.dimension:
            raise ValueError("Points have different dimensions")
        return all([a == b for a, b in zip(self.coords, other.coords)])

    @staticmethod
    def distance(p1, p2):
        if not p1.dimension == p2.dimension:
            raise ValueError("Points have different dimensions")
        return sum([pow(b - a, 2) for a, b in zip(p1.coords, p2.coords)])


Point.NORTH = Point(0, 1)
Point.SOUTH = Point(0, -1)
Point.EAST = Point(1, 0)
Point.WEST = Point(-1, 0)
