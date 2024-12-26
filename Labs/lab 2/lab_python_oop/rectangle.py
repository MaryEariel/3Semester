from .geomobj import GeomObj
from .color import Color

class Rectangle(GeomObj):
    def __init__(self, w, h, r, g, b):
        self.name = "Rectangle"
        self.w = w
        self.h = h
        self.rgb = Color(r, g, b)

    def get_sqr(self):
        return self.w * self.h

    def repr(self):
        return "{}  {} {} {} {} {}".format(self.w, self.h, *self.rgb.get(), self.get_sqr())

    def get_name(self):
        return self.name