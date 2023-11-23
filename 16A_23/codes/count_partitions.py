from pip._internal.models.link import Link


class Link:
    """一个链表"""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest == Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __len__(self):
        return 1 + len(self.rest)

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

def link_expression(s):
    """返回一个可以计算得到 s 的字符串表达式。"""
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)


def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))


def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f, s.first, map_link(f, s.rest))


def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered


def join_link(s, separator):
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)


def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
        Each partition is represented as a linked list.
        """
    if n == 0:
        return Link(Link.empty)  # A list containing the empty partition
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n - m, m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partitions(n, m - 1)
        return with_m + without_m

"""
 正整数 n 的分割数，最大部分为 m，即 n 可以分割为不大于 m 的正整数的和，并且按递增顺序排列
"""
""" 实施 """


def print_partitions(n, m):
    lists = partitions(n, m)
    strings = map_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))
    
    """
    >>> print_partitions(6, 4)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """

    
s = Link(3, Link(4, Link(5)))
print(f"{1}, {2}", 1, 2)
