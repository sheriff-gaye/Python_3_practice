
class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def r_area(l, w):
        return l*w


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def c_area(radius):
        return 3.142*(radius**2)


class Triangel:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def tri_area(self, base, height):
        return 0.5*base*height
