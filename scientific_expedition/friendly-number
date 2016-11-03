# https://github.com/denisbalyko/checkio-solution/blob/master/friendly-number.py
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    index, pow = enumerate(powers)
    # truncate the number, per base and decimals
    if number < base:
        return str(number)
    num = number / base
    print(num)
    # round the number using some unclear rule

    # if there are fewer digits to the right of the decimal than the decimals parameter, pad with 0s

    # append power and suffix
    num = str(num) +



    return str(number)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'

