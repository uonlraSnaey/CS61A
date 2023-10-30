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
