from functools import wraps


def val_checker(callback):
    def _val_checker(func):
        @wraps(func)
        def wrapper(arg):
            if callback(arg):
                return func(arg)
            else:
                raise ValueError(f'wrong val: {arg}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(5)
    print(a)
except ValueError as e:
    print(e)
