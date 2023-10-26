def make_adder():
    def adder(k):
        return k + n
    return adder


def square(x):
    return x * x


def triple(x):
    return 3 * x

def composel(f, g):
    def h(x):
        return f(g(x))
    return h

