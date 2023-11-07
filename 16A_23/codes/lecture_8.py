def pair(x, y):
    def get(index):
        if index == 0:
            return x
        else:
            return y

    return get

def select(p, i):
    return p(i)

p = pair(20, 14)

def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), '分支必须是树'
    return [root_label] + list(branches)

def lable(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

'''
is_tree 函数用于构造函数tree验证所以分支是否结构良好。
'''

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False

    return True

# if_leaf 检查树是否有分支
def is_leaf(tree):
    return not branches(tree)

'''
树递归可用于构造树
首先定义 The nth Fibnacci tree 是指以第n个斐波那契为根标签的树。
……
'''

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = lable(left) + lable(right)
        return tree(fib_n, [left, right])


'''
计树的叶子树
'''
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(brach_counts)

'''
我们可以以 n = 6，m = 4 为例，尝试 “将 6 分割为不超过 4 的若干正整数之和”。首先，所有的分割方式可以被分两类：

(1) 使用至少一个 4 来分割 (2) 使用不超过 3 的若干正整数来分割

让我们再进一步简化

(1) 使用至少一个 4 来分割，即：将 6 先分割出一个 4，再将余下的（6-4）分割为不超过 4 的若干整数之和。 (2) 使用不超过 3 的若干整数来分割，即：“将 6 分割为不超过 3 的若干整数之和”。

于是我们发现，它们都可以抽象出同样的形式，只是参数不同。那么就可以用递归的方法来处理。

除此之外，我们还需明确递归的出口，即什么情况记为分割成功 (True)，什么情况记为分割失败 (False)，包括：

成功分割 n: 即一旦分割后的 n = 0 记为 True 不成功分割 n: 即分割后的 n < 0（比如 n = 2，m = 3 时，用 3 进行分割）记为 False m 递减至 0，不符合正整数的要求，记为 False
'''
def partition_tree(n, m):
    ''' 返回一个分割树， 将n分割为不超过m的若干正整数之和'''
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)

        return tree(m, [left, right])


def print_parts(tree, partition=[]):
    if is_tree(tree):
        if lable(tree):
            print('+'.join(partition))
        else:
            left, right = branches(tree)
            m = str(lable(tree))
            print_parts(left, partition + [m])
            print_parts(right, partition)

'''
>>> print_parts(partition_tree(6, 4))
'''

# 链表具有递归结构
'''
文档测试： python -m doctest -v _.py
>>> 
'''

def count(s, value):
    """
    >>> count([1,2,3,4], 1)
    1
    """

    total = 0
    assert total < 0, 'Invalid value'
    for element in s:
        if element == value:
            total += 1
        return total


