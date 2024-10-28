import math
class BiQuadraticEquation:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
    def get_coef(self):
        """Метод для ввода коэффициентов a, b, c."""
        self.a = float(input("Введите коэффициент a: "))
        self.b = float(input("Введите коэффициент b: "))
        self.c = float(input("Введите коэффициент c: "))
    def solve(self):
        if self.a == 0:
            print("Это не биквадратное уравнение.")
            return
        A = self.a
        B = self.b
        C = self.c
        D = B ** 2 - 4 * A * C
        x_roots = []
        if D < 0:
            print("Нет действительных корней.")
            return
        elif (D == 0):
            y=-B /(2 * A)
            if y >= 0:
                x_roots.append(math.sqrt(y))
                x_roots.append(-math.sqrt(y))
        else:
            y1 = (-B + math.sqrt(D)) / (2 * A)
            y2 = (-B - math.sqrt(D)) / (2 * A)
            if y1 >= 0:
                x_roots.append(math.sqrt(y1))
                x_roots.append(-math.sqrt(y1))
            if y2 >= 0:
                x_roots.append(math.sqrt(y2))
                x_roots.append(-math.sqrt(y2))
        return x_roots

if __name__ == "__main__":
    equation = BiQuadraticEquation()
    equation.get_coef()
    roots = equation.solve()
    if roots:
        print("Корни биквадратного уравнения:", roots)