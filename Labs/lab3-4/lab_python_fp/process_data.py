from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import *

path = "lab_python_fp/data_light.json"

@print_result
def f1(arg):
    return sorted(Unique(field(arg, "job-name"), ignore_case=True))

@print_result
def f2(arg):
    return list(filter(lambda x: "программист" in x.lower()[0:12], arg))

@print_result
def f3(arg):
    return list(map(lambda x: x+" с опытом Python", arg))

@print_result
def f4(arg):
    return list(zip(arg, gen_random(len(arg), 100000, 200000)))