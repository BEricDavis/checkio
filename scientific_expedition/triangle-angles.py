import math


def get_degrees(x, y, z):
    cos = (math.pow(x, 2) + math.pow(y, 2) - math.pow(z, 2))/(2 * x * y)
    return math.degrees(math.acos(cos))


def checkio(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return [0, 0, 0]
    deg_a = int(round(get_degrees(b, c, a)))
    deg_b = int(round(get_degrees(a, c, b)))
    deg_c = int(round(get_degrees(a, b, c)))

    return sorted([deg_a, deg_b, deg_c])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print(checkio(3, 4, 5))
