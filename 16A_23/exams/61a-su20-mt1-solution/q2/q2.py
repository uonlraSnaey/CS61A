email = 'example_key'

def storeroom(radium, fn_even, fn_odd):
    """
    Write a function `storeroom` that takes in a positive integer `radium` and two
    functions `fn_even` and `fn_odd`.

    It applies `fn_even` to all of the even digits in the integer and
    applies `fn_odd` to all of the odd digits in the integer. It then returns whether
    the result of the even values is greater than the result of the odd values.
    You can guarantee that the number has at least one even and odd digit.

    >>> storeroom(1234, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 > 3 * 1
    True
    >>> storeroom(11111111111112, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1 * 1 * ... * 1
    True
    >>> storeroom(11111111111112, lambda x,y: x+y, lambda x,y: x+y) # 2 <= 1 + 1 + ... + 1
    False
    >>> storeroom(12, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1
    True
    >>> storeroom(12345, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 <= 1 * 3 * 5
    False
    >>> storeroom(18383, lambda x,y: x-y, lambda x,y: x-y) # 8 - 8 > 3 - 3 - 1
    True
    """
    evens_defined, odds_defined = False, False
    evens, odds = None, None
    while radium != 0:
        radium, digit = radium // 10, radium % 10
        if digit % 2 == 0:
            if not evens_defined:
                evens = digit
                evens_defined = True
            else:
                evens = fn_even(evens, digit)
        else:
            if not odds_defined:
                odds = digit
                odds_defined = True
            else:
                odds = fn_odd(odds, digit)
    return evens > odds

# ORIGINAL SKELETON FOLLOWS

# def storeroom(radium, fn_even, fn_odd):
#     """
#     Write a function `storeroom` that takes in a positive integer `radium` and two
#     functions `fn_even` and `fn_odd`.

#     It applies `fn_even` to all of the even digits in the integer and
#     applies `fn_odd` to all of the odd digits in the integer. It then returns whether
#     the result of the even values is greater than the result of the odd values.
#     You can guarantee that the number has at least one even and odd digit.

#     >>> storeroom(1234, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 > 3 * 1
#     True
#     >>> storeroom(11111111111112, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1 * 1 * ... * 1
#     True
#     >>> storeroom(11111111111112, lambda x,y: x+y, lambda x,y: x+y) # 2 <= 1 + 1 + ... + 1
#     False
#     >>> storeroom(12, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1
#     True
#     >>> storeroom(12345, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 <= 1 * 3 * 5
#     False
#     >>> storeroom(18383, lambda x,y: x-y, lambda x,y: x-y) # 8 - 8 > 3 - 3 - 1
#     True
#     """
#     evens_defined, odds_defined = False, False
#     evens, odds = None, None
#     while radium != 0:
#         radium, digit = radium // 10, radium % 10
#         if digit % 2 == 0:
#             if not evens_defined:
#                 evens = digit
#                 evens_defined = True
#             else:
#                 evens = fn_even(evens, digit)
#         else:
#             if not odds_defined:
#                 odds = digit
#                 odds_defined = True
#             else:
#                 odds = fn_odd(odds, digit)
#     return evens > odds
