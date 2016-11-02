def checkio(number):
    retval = 1
    for num in str(number):
        num = int(num)
        if num > 0:
            retval *= num
    return retval

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
