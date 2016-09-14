# For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
# Input: A number as an integer.
# Output: The Roman numeral as a string.
# Precondition: 0 < number < 4000


def checkio(data):

    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    num_map = dict(zip(ints, nums))
    result = []
    for i in reversed(sorted(num_map)):
        count = data // i
        result.append(num_map[i] * count)
        data -= i * count
    final = ''.join(result)
    return final


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'