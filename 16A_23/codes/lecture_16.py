class Bank:
    def __init__(self):
        self.accounts = []

    def open_count(self, holder, amount, Kind=Acount):
        account = Kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
    
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_fail(self):
        return len(self.accounts) > 1


class A:
    z = -1
    def f(self, x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)

class C(B):
    def f(self, x):
        return x 

"""

a = A()
b = B(1)
b.n = 5

>>> C(2).n
4

>>> a.z == C.z
True

>>> a.z == b.z
False

子类没有的就在父类上找

"""
