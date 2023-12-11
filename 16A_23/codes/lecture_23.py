def is_prime(x):
    if x <= 1:
        return False
    return all(map(lambda y: x % y, range(2, x)))   # all() 检测 map 函数生成的结果集， 如果所有余数都为真， 则返回 TRUE

def sum_prime(a, b):
    return sum(filter(is_prime, range(a, b)))
 
"""
(define (prime? x)
    (if ( <= x 1)
        false
        (nil? (filter (lambda (y) (= 0 (remainder x y)))
            (range 2 x)))))

(define (sum_prime a b)
    (sum (filter prime? (range a b))))
"""
# recursively define stream is the constant stream 
"""
# The rest of a constant stream is the constant stream 
(define ones (cons-stream 1 ones))

# Combine two stream by separating each into car and cdr

(define (add-stream s t)
    (cons-stream (+ (car s) (car t))
                    (add-stream (cdr-stream s)
                                （cdr-stream t)))

(define ints (cons-stream 1 (add-stream ones ints)))
"""

# heigher order function

"""
(define (sieve s)
    (cons-stream (car-s)
                 (sieve
                 (filter-stream
                 (lambda (x) (not (= 0 (remainder x (car s)))))
                 (cdr-stream s)))))

(define prime (sieve (int-stream 2)))
"""
