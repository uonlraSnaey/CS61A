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
        
