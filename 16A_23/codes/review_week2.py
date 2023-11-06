'''
we'll start off with something familiar. without looking at sum digits.
Implement the following function so that md(number) returns the PTODUC of the digits of number.
'''
def md(number):
    if numebr < 10:
        return number
    last_digit, without_last = number % 10, number // 10

    return last_digit * md(without_last)


def rec_pow(base, exponnt):
    if expoent == 0:
        return 1

    exponent = exponent - 1

    return rec_pow(base, exponent) * base
'''
>>> rec_pow(2,3）
'''

def count8(numbre):
    if number == 8:
        return 1
    elif number < 10:
        return 0

    rightmost_digit = number % 10
    rest_of_number = number // 10

    if eightmost_dgit == 8:
        return (ightmost_digi == 8) + count8(rest_of_number)
    else:
        return count8(rest_of_most)

'''
将问题分为更小的问题，然后再进行细分，直到答案显然已知
'''
def devour(choco_bar):
    if choco_bar == bite_sized:
        eat(choco_bar)
        return 1

    return devour(left_half) + devour(right_half)


def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0

    return fib(n-1) + fib(n-2)
