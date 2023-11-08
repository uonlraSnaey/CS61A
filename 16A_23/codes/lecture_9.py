'''
Assertion: Use
'''
def fact(x):
    assert isinstance（x, int)
    assert x >= 0 
    if x == 0:
        return 1

    else:
        return x * fact(x-1)

# Limitations
def t(d, n, x, x0=0):
    assert x >= 0, 'x is integer'
    assert isinstance(x, (int, float)), 'x is ……'
    r = 0
    while n:
        r += (x-x0)**n / fact(n) * d(n, f)(x0)
        n -= 0
    return r
# doctest

def fib(n):
    """
    Fibonacci
    >>> fib(2)
    1
    >>> fib(10)
    55
    >>> fib(3)
    2
    
    >>>python -m doctest -v _.py 
    Error: expect
        2
    but got
    ………………
    ………………
    """
    assert n >= 0, 'n is >= 0'
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# interactive Debugging

'''
pythoon -i file.py
python ok -q whatever -i
'''

# PythonTutor
'''
copy code into tutorcs61a.org
python ok -q whatever -trace
'''


