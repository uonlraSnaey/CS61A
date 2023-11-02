def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n -1)

'''
continue fixed codes
def krap(n, k):
    if n == 0:
        return k == 0

    last = knap(n // 10, k - n % 10)
    all_but_last = knap(n // 10, k)

    return last or all_but_last
'''


def count_partition(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partition(n-m, m)
        without_m = count_partition(n, m-1)
    
        return with_m + without_m
    
result = count_partition(5, 3)

'''
def all_number(k):
    def h(gm perfix):
        if  k == 0:
            print(perfix)
            return 

        h(k-1, pperfix * 10)
        h(k-1, perfix * 10 + 1)
        

    h(k, 0)

'''

def bin_digit_print(n):
    if n > 0:
        bin_digit_print(n // 2)
        print(n % 2)
    return 

def remove(n, digit):
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if digit != last:
            kept = kept + last  * 10 ** digits
            digits = digits + 1
    return kept
'''
read the template

implement without the template, then change your implementation to match the template
OR
If the template is helpful, use it

Annoate names with calues from your chosen example
write code to compute the result
Did you really return the right thing?
Check your solution with the other examples
'''

