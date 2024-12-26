import abc

class GeomObj(abc.ABC):
    @abc.abstractmethod
    def get_sqr(self): pass