from .geomobj import GeomObj
from .color import Color

class Circle(GeomObj):
    def __init__(self, R, r, g, b):
        self.name = "Circle"
        self.R = R
        self.rgb = Color(r, g, b)

    def get_sqr(self):
        return 3.14 * self.R ** 2

    def repr(self):
        return "{}  {} {} {} {}".format(self.R, *self.rgb.get(), self.get_sqr())

    def get_name(self):
        return self.name