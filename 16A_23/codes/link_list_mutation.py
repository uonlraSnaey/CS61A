def add(s, v):
    """ 向 s 链表中添加整数 v ， 返回修改后的 s """
    """
    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0,Link( 1,Link(3,Link(5))))
    
    >>> add(s, 3)
    Link(0，Link(1，Link(3，Link(5)) ))

    >>> add(s, 4)
    Link(0, Link(1，Link(3,Link( 4，Link(5)))))

    >>> add(s, 6)
    Link(0, Link(1，Link( 3，Link(4，Link(5，Link(6))

    """

    assert s is not List.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest) # 将 v 作为新链表的第一个值（值最小），rest 为旧链表。
    elif s.first < v and empty(s.rest):
        s.rest = Link(v) # s 链表中的值均小于v,且s链表为一个只有第一个值的空链表，最后结果v + s.rest(空值)
    elif s.first < v: # 
        add(s.rest, v) # 直接加在末尾
    return s 

""" Tree mutation"""
def  prune(t, n):
    """ 裁出 label 为 n 的所有子树"""

    t.branches = [b for b.branches if b.label != n]
    for b in t.branches:
        prune(b, n)
