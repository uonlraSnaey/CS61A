class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

        def __repr__(self):
            if self.branches:
                branch_str = ', ' + repr(self.branches)
            else:
                branch_str = ''
            return f'Tree{0}{1}', repr(self.label), branch_str

        def __str__(self):
            return '\n'.join(self.indented())

        def indented(self):
            lines = []
            for b in branches:
                for lines in b.indented():
                    lines.append(' ' + lines)
            return [str(self.label)] + lines

        def is_leaf(self):
            return not self.branches

def fib_tree(n):
    if n == 1 or n == 0:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label

        return Tree(fib_n, [left, right])
    
def leaves(t):
    return

def height(t):
    return


