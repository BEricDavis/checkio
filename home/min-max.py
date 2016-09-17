# In this mission you should write you own py3 implementation (but you can use py2 for this) of the built-in
#  functions min and max. Some builtin functions are closed here: import, eval, exec, globals.
# Don't forget you should implement two functions in your code.
# max(iterable, *[, key]) or min(iterable, *[, key])
# max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])


def min(*args, **kwargs):
    print('\n')
    print('args = {} {}'.format(args, type(args)))
    print('kwargs = {} {}'.format(kwargs, type(kwargs)))
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = list(args[0])


    value = sorted(args)[0]
    # print('value = {} {}'.format(value, type(value)))
    # if type(value) is list:
    #     value = sorted(value)[0]
    # if type(value) is str:
    #     value = sorted(value)[0]
    print('value = {} {}'.format(value, type(value)))
    return value


def max(*args, **kwargs):
    print('\n')
    print('args = {} {}'.format(args, type(args)))
    print('kwargs = {} {}'.format(kwargs, type(kwargs)))
    key = kwargs.get("key", None)

    if len(args) == 1:
        args = list(args[0])

    value = sorted(args)[-1]
    # print('value = {} {}'.format(value, type(value)))
    #
    # if type(value) is list:
    #     value = sorted(value)[-1]
    # if type(value) is str:
    #     value = sorted(value)[-1]
    if key:
        print('key = {}'.format(key))
        value = key(value)
    print('value = {} {}'.format(value, type(value)))
    return value


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
