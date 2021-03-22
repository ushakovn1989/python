from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        all_args = (i for i in (*args, *kwargs.values()))
        return f'{func.__name__}({", ".join(map(lambda arg: str(f"{arg}: {type(arg)}"), all_args))})'

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
