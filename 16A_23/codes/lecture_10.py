import doctest
def tree(root_lable, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_lable] + list(branches)


def lable(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    """
    is_tree([1, 2, 3])
    True
    """
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
        

def is_leaf(tree):
    """
    is_leaf([1, 2, 3])
    False
    """
    return not branches(tree)


def fib_tree(n):
    """
    fib_tree(5)
    [5, [3, [1, [1, [1, [True], [False]], [False]], [False]], [2, [1, [True], [False]], [False]]], [4, [2, [1, [True], [False]], [False]], [3, [1, [True], [False]], [False]]]]
    """
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = lable(left) + lable(right)
        return tree(fib_n, [left, right])


def count_leaves(tree):
    """
    count_leaves(fib_tree(5))
    8
    """
    if is_leaf:
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)
    

def partition_tree(n, m):
    """
    
    """
    # 返回一个分割树， 将n分割为不超过m的若干正整数之和
    if n == 0:
        return tree(True)
    
    elif n < 0 or m == 0:
        return tree(False)
    
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        
        return tree(m, [left, right])
    

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if lable(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(lable(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)
        

"""
Q:
Define the function add_trees, which takes in two trees and returns a new tree where each corresponding node from the first tree is added with the node from the second tree. If a node at any particular position is present in one tree but not the other, it should be present in the new tree as well.

Hint: You may want to use the built-in zip function to iterate over multiple sequences at once.

Note: If you feel that this one's a lot harder than the previous tree problems, that's totally fine! This is a pretty difficult problem, but you can do it! Talk about it with other students, and come back to it if you need to.
"""
def add_tree(t1, t2):
    """   
    Hint: You may want to use the built-in zip function to iterate over multiple sequences at once.
    Note: If you feel that this one's a lot harder than the previous tree problems, that's totally fine! This is a pretty difficult problem, but you can do it! Talk about it with other students, and come back to it if you need to.
    >>> number = tree(1,
                    [tree(2,
                        [tree(3),
                        tree(4)],
                    tree(5,
                        [tree(6,
                            [tree(7)]),
                        tree(8)])])
    >>> print_tree(add_trees(number, number))
    2
     4
      6
      8
    10
      12
        14
      16
    """
    if is_leaf(t1):
        return tree(label(t1) + label(t2), branches(t1))
    if is_tree(t2):
        return tree(label(t1) + label(t2), branches(t2))
    else:
        fwer, more = sorted([branch(t1), branches(t2)], key=len)
        
        added_t1 = fwer + [tree(i) for i in range(len(more) - len(fwer))]
        added_t2 = more

        return tree(label + label(t2), [add_tree(a,b) for a, b in zip(added_t1, added_t2)])


