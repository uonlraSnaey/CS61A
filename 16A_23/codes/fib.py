def fib(n):
    pred, curr = 0, 1
    k = 2
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr


result = fib(8)