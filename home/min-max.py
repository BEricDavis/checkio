# In this mission you should write you own py3 implementation (but you can use py2 for this) of the built-in
#  functions min and max. Some builtin functions are closed here: import, eval, exec, globals.
# Don't forget you should implement two functions in your code.
# max(iterable, *[, key]) or min(iterable, *[, key])
# max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])


def compare_min(x, y, key):
    # If there is a key, use it
    if key is not None:
        if key(y) > key(x):
            return x
    else:
        if y > x:
            return x
    return y


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    # if args is only one item it's probably a container or a string...
    if len(args) == 1:
        # ...so make it a list.
        args = list(args[0])

    value = sorted(args)[0]

    for arg in range(1, len(args)):
        value = compare_min(value, args[arg], key)

    return value


def compare_max(x, y, key):
    print('compare_max: {}, {}, {}'.format(x, y, key))
    # If there is a key, use it
    if key is not None:
        if key(y) > key(x):
            return y
    else:
        if y > x:
            return y
    return x


def max(*args, **kwargs):
    key = kwargs.get("key", None)

    # if args is only one item it's probably a container or a string...
    if len(args) == 1:
        # ...so make it a list
        args = list(args[0])

    value = args[0]

    for arg in range(1, len(args)):
        value = compare_max(value, args[arg], key)

    return value


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
