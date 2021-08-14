
def type_logger(func):

    def wrapp(*args):
        dict_decor = {args[key]: type(args[key]) for key in range(len(args))}
        return dict_decor
    return wrapp


@type_logger
def calc_cube(*num):
    list_1 = [i for i in num]
    return [i ** 3 for i in list_1]


calc = calc_cube(5, 1, 4, 8.6, 'a')
print(calc)
print()
