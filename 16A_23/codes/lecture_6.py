def sum_unique(n):
    result = 0
    while n > 0:
        last, all_not_last, include = n % 10, n // 10, True
        while all_not_last > 0:
            if last == all_not_last % 10:
                include = False
            all_not_last = all_not_last // 10
        if include:
            result = result + last
        n //= 10
    return result
def make_adder(n):
    def adder(x):
        return x + n
    return adder

'''
>>> add_5 = make_adder(5)
>>> add_5(3)
6
'''

def sum_all(a):
    def sum_first(b):
        def sum_scond(c):
            c = c // 10
            def sum_third(d):
                    d += 1
                def sum_five(f):
                    f = f + "!" 
                    if f == "done":
                        return a

                    return a + c +
                     b + d + f
                return sum_five
             return sum_third
        return sum_scond
    return sun_first
result = sum_all(1)(2)(3)("done")
lambda_value = sum_all(lambda a: a+2)(lambda b: b*b)


def do_all(f):
    def g(x):
        if x == "done":
            return f 
        return do_all(then(f, x))
    return g

def then(f, g):
    def h(x):
        return f(g(x))
    return h
a_value = do_all(lambda x: x + 3)(lambda x: x**2)(lambda x: x * (-1)): ("done")

# '斐波那契数的和
fibonacci = lambda x: lambda y: x if x <= 1 else fibonacci(y)(x+y)

'''
n为第n个斐波那契数

'''n = 10
result = fibonacci(0)(1)(n)

