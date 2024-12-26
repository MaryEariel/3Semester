import json
from lab_python_fp.sort import sort
from lab_python_fp.cm_timer import *
from lab_python_fp.process_data import *

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    print("field.py")
    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))
    print()

    print("gen_random.py")
    print(*gen_random(5, 1, 3))
    print()

    print("unique.py")
    out = gen_random(50, 1, 30)
    print("out:", *out)
    ls = Unique(out, ignore_case=1)
    for el in ls: print(el, end=" ")
    print("\n-")
    for el in ls: print(el, end=" ")
    print("\n")

    print("sort.py")
    result = sort(data)
    print("lambda ", result)
    result_with_lambda = sorted(data, reverse=True)
    print("reverse", result_with_lambda)
    print()

    print("print_result.py")
    print("test_1 res", test_1())
    print("test_2 res", test_2())
    print("test_3 res", test_3())
    print("test_4 res", test_4())
    print()

    print("cm_timer.py")
    with cm_timer_1():
        time.sleep(1.5)

    with cm_timer_2().maneger():
        time.sleep(2.5)
    print()

    print("process_data.py")
    with open(path) as f:
        data = json.load(f)
    with cm_timer_1():
        f4(f3(f2(f1(data))))