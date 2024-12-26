from .rectangle import Rectangle

class Squere(Rectangle):
    def __init__(self, a, r, g, b):
        super().__init__(a,a,r,g,b)
        self.name = "Squere"

    def get_sqr(self):
        return self.w * self.w

    def repr(self):
        return "{}  {} {} {} {}".format(self.w, *self.rgb.get(), self.get_sqr())

    def get_name(self):
        return self.name