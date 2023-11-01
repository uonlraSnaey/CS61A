def curried_pow(x):
    def f(y):
        return pow(x, y)
    return f


def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1


def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last


def mul_co(n):
    if n == 0:
        return 1
    else:
        return n * mul_co(n - 1)

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)


def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)

def is_even(n):
    if n == 0:
        return True
    else:
        if (n-1) == 0:
            return False
        else:
            return is_even((n-1) - 1)


def cascade(n):
    print(n)
    if n > 10:
        cascade(n//10)
        print(n)


def play_alice(n):
    if n == 0:
        print("Bob wins")
    else:
        play_bob(n-1)


def play_bob(n):
    if n == 0:
        print("Alice wins")
    elif is_even(n):
        play_alice(n-2)
    else:
        play_alice(n-1)


""" 斐波那契几何模型"""
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def count_partition(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return (count_partition(n-m, m) +
                count_partition(n, m - 1))


def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


def sum_cube(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total


def split(x):
    return n // 10. n % 10

def sun_all__digital(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_all_digital(all_but_last) + last


def lum_sum(m):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last)

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digital(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

"""
迭代是递归的特殊情况,大多数情况递归可以直接转换为迭代

Can be tricky: Iteration is a sprcial case of reccusion
Idea: Figure out what state must be maintained by the iterative function

使用while将迭代转化为递归要简单得多

"""

def sum_digit_iter(n):
    digit_sum = 0:
        while n >0:
            n, last = split(n)
            digit_sum = digit_sum + last
    return figit_sum
# 上式为迭代(循环替换），下式为递归(反复调用，最后相加）
def sum_digit_rec(n, digit_sum):
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digit_rec(n, digit_sum + last)


'''
def cascade(n):
    if  n < 10:
        print(n)
    else:
        print(n)
        cascade(m//10)
        print(n)
'''

def cascade(n):
    print(n)
    if n > 10:
        cascade(n//10)
        print(n)

"""
write a function that print an inverse cascade

1
12
123
1234
123
12
1

"""

def cascade_moer(n, x=1, direction=1):
    if x == n:
        derection = -1
    for i in range(1, x + 1):
        print(i)
    if x > 1:
        cascade(n ,x-1, direction)
    eelif direction == 1:
        cascade(n, x + 1, direction)

def curried_po2(x=2):
    def h(y):
        return pow(x, y)
    return h
