
def make_zipper(f1, f2, sequence):
    """
    We would like to create a function make_zipper that takes two functions f1(x) and f2(x) and a "zipper
    sequence", which is a number that contains a series of 1s and 2s. It returns a function that is the equivalent of
    f1(f2(f2(...f1(x)...))) in which the exact sequence of f1s and f2s is given by the digits of the sequence.
    As an example, if the sequence were 1211, that would mean return a function of x that is the equivalent to
    f1(f2(f1(f1(x)))). Neither recursion nor containers (lists, dictionaries, sets, etc) are allowed in your solution.

    Return a function of f1 and f2 composed based on sequence.
    >>> increment = lambda x: x + 1
    >>> square = lambda x: x * x
    >>> do_nothing = make_zipper(increment, square, 0)
    >>> do_nothing(2) # Don't call either f1 or f2, just return your input untouched
    2
    >>> incincsq = make_zipper(increment, square, 112)
    >>> incincsq(2) # increment(increment(square(2))), so 2 -> 4 -> 5 -> 6
    6
    >>> sqincsqinc = make_zipper(increment, square, 2121)
    >>> sqincsqinc(2) # square(increment(square(increment(2)))), so 2 -> 3 -> 9 -> 10 -> 100
    100
    """
    """
    make_zipper(f1(x), f2(x), zipper sequence)
    return a function: 等价于 f1(f2(f2(...f1(x)...))) , f1 和 f2 的使用次序由这个数字 决定 
    举个例子，如果序列是 1211，那意味着返回的函数将相当于 f1(f2(f1(f1(x))))
    换句话说，这个函数 make_zipper 的任务是基于给定的数字序列，将 f1 和 f2 以特定的顺序组合起来，最终返回一个函数，这个函数对输入 x 进行连续的 f1 和 f2 的嵌套调用。

    """
    # zipper = x 
    zipper = lambda x: x
    helper = lambda f, g: lambda x: f(g(x)) 
    while sequence:
        if sequence % 10 == 1:
            zipper = helper(f1, zipper)
        else:
            zipper = helper(f2, zipper)

        sequence = sequence // 10 
    return zipper

# ORIGINAL SKELETON FOLLOWS

# def make_zipper(f1, f2, sequence):
#     """
#     We would like to create a function make_zipper that takes two functions f1(x) and f2(x) and a "zipper
#     sequence", which is a number that contains a series of 1s and 2s. It returns a function that is the equivalent of
#     f1(f2(f2(...f1(x)...))) in which the exact sequence of f1s and f2s is given by the digits of the sequence.
#     As an example, if the sequence were 1211, that would mean return a function of x that is the equivalent to
#     f1(f2(f1(f1(x)))). Neither recursion nor containers (lists, dictionaries, sets, etc) are allowed in your solution.

#     Return a function of f1 and f2 composed based on sequence.
#     >>> increment = lambda x: x + 1
#     >>> square = lambda x: x * x
#     >>> do_nothing = make_zipper(increment, square, 0)
#     >>> do_nothing(2) # Don't call either f1 or f2, just return your input untouched
#     2
#     >>> incincsq = make_zipper(increment, square, 112)
#     >>> incincsq(2) # increment(increment(square(2))), so 2 -> 4 -> 5 -> 6
#     6
#     >>> sqincsqinc = make_zipper(increment, square, 2121)
#     >>> sqincsqinc(2) # square(increment(square(increment(2)))), so 2 -> 3 -> 9 -> 10 -> 100
#     100
#     """
#     zipper = ______
#     helper = ______
#     while ______:
#         if ______ == 1:
#             zipper = helper(f1, ______)
#         else:
#             zipper = helper(f2, ______)
#         sequence = ______
#     return zipper
