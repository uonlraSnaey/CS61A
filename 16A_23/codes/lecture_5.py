from operator import mul
def squre(x):
    return mul(x, x)

def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3

def make_adder(n):
    def adder(k):
        return k + n
    return adder

"""
NESTS FUNCTION

create a function value: func <name> (<formal parameters>)[parent=<parent>]
Its paret is he curent grame
bind <name> to the function value in the current frame
when a function called:
1.Add a local frame , titeld with the <naem> of the function beging called
2.Copy the parent of the function to the local frame: [parent = <labe>l]
3.Bind the <formal parameter> to the arguments in the local frame
4. Excutethe body of the function in the environmenyt that starts with the local frame
"""
def f(x, y):
    return g(x)

def g(x):
    return x + y
first_value = lambda x : x*x
sec_value = lambda f, g: f + g

def print_all(x):
    print(x)
    def next_sum(y):
        return print_sum(x +y)
    return next_sum
# ptint(1)(2)(3)

def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

mask = lambda horse: horse(2)

horse(mask)


def tracel(fn):
    def traced(x):
        print(f" now is calling {fn}, on argument {x}")
        return fn(x)
    return traced

# @tracel
def square(x):
    return x * x
square = trace[square]

@tracel
def sum_square_up_to(n):
    k , total = 1, 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total
