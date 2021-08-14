import functools


def val_checker(func):

    @functools.wraps(func)
    def wrapp(num):
        if num < 0:
            raise ValueError(f'Wrong val {num}')
        else:
            print(func(num))
    return wrapp


@val_checker
def calc_cube(num):
    return num ** 3


try:
    a = calc_cube(8)
    print(type(calc_cube))
    print(help(calc_cube))
except (ValueError, TypeError) as e:
    print(e)
