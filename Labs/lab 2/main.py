from colorama import Fore
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.squere import Squere

if __name__ == "__main__":
    rect = Rectangle(8, 8, 0, 0, 255)
    crcl = Circle(8, 0, 255, 0)
    sqr = Squere(8, 255, 0, 0)
    print(Fore.BLUE+rect.get_name(), rect.repr())
    print(Fore.GREEN+crcl.get_name(), crcl.repr())
    print(Fore.RED+sqr.get_name(), sqr.repr())