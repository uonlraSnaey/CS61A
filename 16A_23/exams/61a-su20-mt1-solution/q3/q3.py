email = 'example_key'

def maxkd(meteor, k):
    """
    Given a number `meteor`, finds the largest number of length `k` or fewer,
    composed of digits from `meteor`, in order.

    >>> maxkd(1234, 1)
    4
    >>> maxkd(32749, 2)
    79
    >>> maxkd(1917, 2)
    97
    >>> maxkd(32749, 18)
    32749
    """
    if meteor == 0 or k == 0:
        return 0
    a = (meteor % 10) maxkd(meteor // 10, k - 1) * 10
    b = maxkd(meteor // 10, k)
    return a if a > b else b
# ORIGINAL SKELETON FOLLOWS

# def maxkd(meteor, k):
#     """
#     Given a number `meteor`, finds the largest number of length `k` or fewer,
#     composed of digits from `meteor`, in order.

#     >>> maxkd(1234, 1)
#     4
#     >>> maxkd(32749, 2)
#     79
#     >>> maxkd(1917, 2)
#     97
#     >>> maxkd(32749, 18)
#     32749
#     """
#     if meteor == 0 or k == 0:
#         return 0
#     a = maxkd(meteor // 10, k - 1) * 10 + meteor % 10
#     b = maxkd(meteor // 10, k)
#     return max(a, b)
