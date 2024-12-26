def print_result(func):
    def wrapper(*args, **kwargs):
        out = func(*args, **kwargs)
        print("-"*10)
        print(func.__name__)
        if type(out) == type([]): print(*out, sep="\n")
        elif type(out) == type({}): print(*[f"{el} = {out[el]}" for el in out], sep="\n")
        else: print(out, sep="\n")
        print("-"*10)
        return out
    return wrapper


@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]